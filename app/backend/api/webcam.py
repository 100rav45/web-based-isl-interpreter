from fastapi import APIRouter, UploadFile, File
import cv2
import numpy as np

from app.backend.schemas import PredictionResult
from app.backend.services.image_prediction_service import (
    image_prediction_service
)

router = APIRouter()


@router.post(
    "/predict-frame",
    response_model=PredictionResult
)
async def predict_frame(
    file: UploadFile = File(...)
):
    try:
        image_bytes = await file.read()

        print("Uploaded bytes:", len(image_bytes))

        image = cv2.imdecode(
            np.frombuffer(image_bytes, np.uint8),
            cv2.IMREAD_COLOR
        )

        if image is None:
            print("❌ OpenCV failed to decode image")
        else:
            print("✅ Image decoded:", image.shape)

        result = image_prediction_service.predict(image)

        print(result)

        return result

    except Exception as e:
        import traceback
        traceback.print_exc()
        raise