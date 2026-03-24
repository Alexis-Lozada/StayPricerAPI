from fastapi import APIRouter, HTTPException
from app.models.prediction_schemas import StayFeatures, PredictionResponse
from app.services.prediction_service import prediction_service

router = APIRouter()

@router.post("/predict", response_model=PredictionResponse)
async def predict_price(data: StayFeatures):
    """
    Endpoint that suggests a price based on capacity, rooms and bathrooms.
    """
    try:
        suggested_price = prediction_service.predict(data)
        
        return PredictionResponse(
            suggested_price=suggested_price,
            currency="MXN"
        )
    except RuntimeError as re:
        raise HTTPException(status_code=500, detail=str(re))
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error processing prediction: {str(e)}")
