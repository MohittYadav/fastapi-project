from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


def register_exception_handlers(app: FastAPI):
    @app.exception_handler(Exception) # This decorator registers a global exception handler for all unhandled exceptions in the FastAPI application.
    async def generic_exception_handler(request: Request, exc: Exception):
        return JSONResponse(
            status_code=500,
            content={'detail': str(exc)},
        )