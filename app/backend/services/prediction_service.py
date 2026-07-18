from app.backend.model_loader import model_loader


class PredictionService:

    def __init__(self):

        self.model, self.label_encoder = model_loader.load()

    def predict(self, features):

        prediction = self.model.predict(
            [features]
        )[0]

        confidence = self.model.predict_proba(
            [features]
        )[0].max()

        label = self.label_encoder.inverse_transform(
            [prediction]
        )[0]

        return {

            "prediction": label,

            "confidence": round(
                float(confidence * 100),
                2
            )

        }


prediction_service = PredictionService()