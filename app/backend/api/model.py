import json

from fastapi import APIRouter

from app.backend.config import MODEL_INFO_FILE

router = APIRouter()


@router.get("/model-info")
def model_info():

    with open(MODEL_INFO_FILE, "r") as f:
        info = json.load(f)

    return info