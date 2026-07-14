from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.core.logging import setup_logging

def get_application() -> FastAPI:
    # Initialize Logging
    setup_logging()
    
    _app = FastAPI(
        title=settings.PROJECT_NAME,
        openapi_url=f"{settings.API_V1_STR}/openapi.json",
        debug=settings.DEBUG
    )

    # Set all CORS enabled origins
    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS] or ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @_app.get("/health", tags=["Health"])
    async def health_check():
        return {"status": "healthy", "service": settings.PROJECT_NAME}

    return _app

app = get_application()