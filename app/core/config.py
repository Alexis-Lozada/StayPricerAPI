import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """
    Project settings and configuration.
    """
    PROJECT_NAME: str = "StayPricerAPI"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    
    # Model paths
    BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    MODEL_PATH: str = os.path.join(BASE_DIR, "ml_models", "model.keras")
    SCALER_PATH: str = os.path.join(BASE_DIR, "ml_models", "scaler.npz")

    class Config:
        env_file = ".env"

settings = Settings()
