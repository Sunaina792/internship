from fastapi import FastAPI, HTTPException
from app.routers import books, authers
from app.exceptions.handlers import http_exception_handler, validation_exception_handler
from app.exceptions import RequestValidationsionError



app = FastAPI(
    title = "FastAPI Application",
    description = "An example FastAPI application with modular routers and custom exception handling.",
    version = "1.0.0"
)

# Include routers
app.add_exception