import numpy as np
import tensorflow as tf
from sklearn.preprocessing import StandardScaler
from app.core.config import settings
from app.models.prediction_schemas import StayFeatures

class PredictionService:
    def __init__(self):
        self.model = None
        self.scaler = None

    def load_model(self):
        """
        Load the Keras model and the scaler parameters from disk.
        """
        try:
            # Load the Keras model
            self.model = tf.keras.models.load_model(settings.MODEL_PATH)
            
            # Reconstruct the StandardScaler with saved parameters
            params = np.load(settings.SCALER_PATH)
            self.scaler = StandardScaler()
            # Assigning mean and scale learned during training
            self.scaler.mean_ = params["mean"]
            self.scaler.scale_ = params["scale"]
            
            print(f"✅ Model and scaler loaded successfully from {settings.BASE_DIR}.")
        except Exception as e:
            print(f"❌ Error loading model files: {e}")
            raise e

    def predict(self, features: StayFeatures) -> float:
        """
        Perform a prediction based on the input features.
        """
        if self.model is None or self.scaler is None:
            raise RuntimeError("Model or scaler not loaded.")

        # 1. Transform input JSON to a NumPy array
        input_data = np.array([[features.capacity, features.rooms, features.bathrooms]])
        
        # 2. Scale the data exactly as in training
        scaled_data = self.scaler.transform(input_data)
        
        # 3. Perform prediction
        prediction = self.model.predict(scaled_data)
        
        # 4. Extract the prediction value (Keras returns a 2D array)
        estimated_price = float(prediction[0][0])
        
        return round(estimated_price, 2)

# Global instance for the service
prediction_service = PredictionService()
