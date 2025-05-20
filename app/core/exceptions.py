from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi import status
from fastapi.exception_handlers import RequestValidationError
from fastapi.exceptions import RequestValidationError

async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "message": "Dados inválidos.",
            "errors": exc.errors()
        }
    )
