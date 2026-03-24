import numpy as np
import tensorflow as tf
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sklearn.preprocessing import StandardScaler
from contextlib import asynccontextmanager

# Variables globales para almacenar el modelo y el escalador en memoria
modelo = None
scaler = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global modelo, scaler
    try:
        # Cargar el modelo Keras
        modelo = tf.keras.models.load_model("modelo_precios.keras") 
        
        # Reconstruir el StandardScaler con los parámetros guardados
        params = np.load("scaler_params.npz")
        scaler = StandardScaler()
        # Se asignan las medias y varianzas aprendidas durante el entrenamiento
        scaler.mean_ = params["mean"]
        scaler.scale_ = params["scale"]
        
        print("✅ Modelo y scaler cargados correctamente en memoria.")
    except Exception as e:
        print(f"❌ Error al cargar los archivos: {e}")
    
    yield # Aquí es donde FastAPI maneja las peticiones web
    
    # Limpieza al apagar el servidor (opcional)
    modelo = None
    scaler = None

# Inicializar la aplicación
app = FastAPI(
    lifespan=lifespan, 
    title="StayPricerAPI",
    description="API que sugiere un precio basado en capacidad, habitaciones y baños."
)

# Definir el esquema de datos de entrada con Pydantic
class CaracteristicasHospedaje(BaseModel):
    capacidad: int
    habitaciones: int
    banos: float

@app.post("/predecir")
async def predecir_precio(datos: CaracteristicasHospedaje):
    # Validar que la IA esté lista
    if modelo is None or scaler is None:
        raise HTTPException(status_code=500, detail="El modelo no está disponible.")

    try:
        # 1. Transformar el JSON de entrada a un array de NumPy
        nuevo_dato = np.array([[datos.capacidad, datos.habitaciones, datos.banos]])
        
        # 2. Escalar los datos exactamente como en el entrenamiento
        dato_escalado = scaler.transform(nuevo_dato)
        
        # 3. Realizar la predicción
        prediccion = modelo.predict(dato_escalado)
        
        # 4. Extraer el valor de la predicción (Keras devuelve un array 2D)
        precio_estimado = float(prediccion[0][0])
        
        return {
            "precio_sugerido": round(precio_estimado, 2),
            "moneda": "MXN" # Opcional: ajusta la moneda según tu dataset
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al procesar la predicción: {str(e)}")