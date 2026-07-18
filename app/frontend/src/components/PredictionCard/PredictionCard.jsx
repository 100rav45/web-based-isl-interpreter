import "./PredictionCard.css";

export default function PredictionCard({ result }) {

    if (!result) return null;

    const noHand =
        result.prediction === null ||
        result.prediction === undefined ||
        result.prediction === "No Hand";

    return (

        <div className="prediction-card">

            <div className="prediction-header">

                {noHand ? "⚠ No Hand Detected" : "✅ Prediction Successful"}

            </div>

            <h1 className="prediction-letter">

                {result.prediction ?? "No Hand"}

            </h1>

            <div className="prediction-details">

                <div className="detail-box">

                    <span className="detail-title">

                        🎯 Confidence

                    </span>

                    <h3>

                        {result.confidence ?? 0}%

                    </h3>

                </div>

                <div className="detail-box">

                    <span className="detail-title">

                        ⏱ Processing Time

                    </span>

                    <h3>

                        {result.processing_time_ms ?? 0} ms

                    </h3>

                </div>

                <div className="detail-box">

                    <span className="detail-title">

                        🤖 Model

                    </span>

                    <h3>

                        Random Forest

                    </h3>

                </div>

            </div>

        </div>

    );

}