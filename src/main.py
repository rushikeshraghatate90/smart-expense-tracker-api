from fastapi import FastAPI

from .routes import router
from .storage import initialize_storage

app = FastAPI(
    title="Smart Expense Tracker API",
    description="A REST API for managing personal expenses.",
    version="1.0.0",
)

initialize_storage()

app.include_router(router)


@app.get(
    "/",
    tags=["Root"],
    summary="API Home",
)
def root() -> dict[str, str]:
    """
    Root endpoint providing basic API information.
    """
    return {
        "message": "Welcome to Smart Expense Tracker API",
        "documentation": "/docs",
        "version": "1.0.0",
    }