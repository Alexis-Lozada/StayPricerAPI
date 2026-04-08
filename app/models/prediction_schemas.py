from pydantic import BaseModel

class StayFeatures(BaseModel):
    """
    Schema for input data for price prediction.
    """
    capacity: int
    rooms: int
    bathrooms: float
    beds: int
    latitude: float
    longitude: float

class PredictionResponse(BaseModel):
    """
    Schema for the response of the prediction API.
    """
    suggested_price: float
    currency: str = "MXN"
