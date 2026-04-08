# StayPricerAPI

Microservicio basado en FastAPI que utiliza un modelo de Keras/TensorFlow entrenado para sugerir precios de alojamiento basados en capacidad, habitaciones y baños.

## Caracteristicas

- Integracion de Machine Learning: Prediccion de precios en tiempo real utilizando un modelo de Keras pre-entrenado.
- Arquitectura Modular: Separacion clara de responsabilidades (API, Servicios, Modelos, Core).
- Estandares Internacionales: Codigo base traducido al ingles para mayor compatibilidad.
- Versionado: Documentacion de la API versionada bajo /api/v1/.
- Listo para Docker: Facil contenedorizacion para un despliegue consistente.

## Estructura del Proyecto

```text
stay-pricer-api/
├── app/
│   ├── main.py            # Punto de entrada: inicializa FastAPI e incluye routers
│   ├── api/               # Controladores/Routers de la API
│   │   └── v1/
│   │       └── prediction_router.py
│   ├── core/              # Configuracion y constantes
│   ├── models/            # Esquemas de Pydantic (formas de datos)
│   ├── services/          # Logica de negocio: carga de modelos y prediccion
│   └── ml_models/         # Almacenamiento de archivos .keras y .npz
├── .dockerignore
├── .env                  # Variables de entorno
├── Dockerfile            # Configuracion del contenedor
├── requirements.txt      # Dependencias del proyecto
└── README.md             # Este archivo
```

## Instalacion Local

### Prerrequisitos
- Python 3.13 (o version compatible)

### Pasos
1. Clonar el repositorio:
   ```bash
   git clone https://github.com/Alexis-Lozada/StayPricerAPI.git
   cd stay-pricer-api
   ```

2. Crear y activar un entorno virtual:
   ```bash
   python -m venv venv
   # En Windows:
   .\venv\Scripts\Activate.ps1
   # En Linux/macOS:
   source venv/bin/activate
   ```

3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Ejecutar la aplicacion:
   ```bash
   uvicorn app.main:app --reload
   ```

---

## Uso con Docker

1. Construir la imagen:
   ```bash
   docker build -t stay-pricer-api .
   ```

2. Ejecutar el contenedor:
   ```bash
   docker run -d -p 8000:8000 --name stay-pricer-api stay-pricer-api
   ```

---

## Uso de la API

Una vez en ejecucion, accede a la documentacion interactiva automatica en:
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

### Ejemplo de Peticion

POST /api/v1/predict

```json
{
  "capacity": 4,
  "rooms": 2,
  "bathrooms": 1.5,
  "beds": 2,
  "latitude": 19.4326,
  "longitude": -99.1332
}
```

### Ejemplo de Respuesta

```json
{
  "suggested_price": 1250.50,
  "currency": "MXN"
}
```

---

## Licencia

Distribuido bajo la Licencia MIT. Consulta el archivo LICENSE para mas informacion (si aplica).
