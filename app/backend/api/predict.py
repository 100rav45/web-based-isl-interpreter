from fastapi import (
    APIRouter,
    UploadFile,
    File
)

import cv2
import numpy as np
import time

from app.backend.schemas import PredictionResult

from app.backend.services.image_prediction_service import (
    image_prediction_service
)

router = APIRouter()


@router.post(
    "/predict-image",
    response_model=PredictionResult
)
async def predict_image(

    file: UploadFile = File(...)

):

    image_bytes = await file.read()

    image = cv2.imdecode(

        np.frombuffer(
            image_bytes,
            np.uint8
        ),

        cv2.IMREAD_COLOR

    )
    print(image.shape)

    cv2.imwrite("debug_uploaded.jpg", image)

    print("Saved uploaded image.")

    start = time.perf_counter()
    
    result = image_prediction_service.predict(image)

    elapsed = (time.perf_counter() - start) * 1000

    if result["prediction"] is None:

        result["success"] = False

        result["message"] = "No hand detected."

    else:

        result["success"] = True

        result["message"] = "Prediction successful."
        
    result["processing_time_ms"] = round(elapsed, 2)

    return result