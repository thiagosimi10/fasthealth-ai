from fastapi import FastAPI
from api.v1.patient_router import router as patient_router
from api.v1.predict_router import router as predict_router
from core.database import Base, engine
from core.exceptions import validation_exception_handler
from fastapi.exceptions import RequestValidationError
from services.cache_service import PatientCacheService

app = FastAPI(
    title="FastHealth AI",
    version="1.0.0",
    description="AI-powered health analytics API"
)

# Routers
app.include_router(patient_router)
app.include_router(predict_router)

# Exception handler
app.add_exception_handler(RequestValidationError, validation_exception_handler)

@app.on_event("startup")
async def startup():
    # Criação das tabelas
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    # Inicializa conexão Redis
    await PatientCacheService.connect()

@app.on_event("shutdown")
async def shutdown():
    await PatientCacheService.disconnect()
