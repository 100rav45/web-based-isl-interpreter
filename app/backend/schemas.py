from pydantic import BaseModel
from typing import List
from pydantic import BaseModel


class PredictionRequest(BaseModel):

    features: List[float]


class PredictionResponse(BaseModel):

    prediction: str

    confidence: float

from pydantic import BaseModel


class PredictionResult(BaseModel):

    prediction: str

    confidence: float

    processing_time_ms: float | None = None