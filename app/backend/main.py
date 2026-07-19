from fastapi import FastAPI

from app.backend.api.health import router as health_router
from app.backend.model_loader import model_loader
from app.backend.api.model import router as model_router
from app.backend.api.predict import router as predict_router
from app.backend.api.webcam import router as webcam_router
from app.backend.exceptions import global_exception_handler
from app.backend.middleware import logging_middleware
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="ISL Translator API",
    version="2.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://your-vercel-app.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.middleware("http")(
    logging_middleware
)

app.add_exception_handler(Exception, global_exception_handler)

@app.on_event("startup")
def startup():

    model_loader.load()

@app.get("/")
def root():

    return {
        "message": "ISL Translator API Running"
    }


app.include_router(
    health_router
)
app.include_router(
    model_router
)
app.include_router(
    predict_router
)
app.include_router(
    webcam_router
)