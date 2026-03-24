from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.core.config import settings
from app.api.v1.prediction_router import router as api_v1_router
from app.services.prediction_service import prediction_service

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Handle startup and shutdown events.
    """
    # Load the model and scaler on startup
    prediction_service.load_model()
    
    yield # API handles requests here
    
    # Optional cleanup on shutdown
    pass

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="API that suggests a price based on capacity, rooms and bathrooms.",
    lifespan=lifespan
)

# Include API routers
app.include_router(api_v1_router, prefix=settings.API_V1_STR)

@app.get("/health", tags=["System"])
async def health_check():
    """
    Simple health check endpoint.
    """
    return {"status": "ok", "project": settings.PROJECT_NAME}
