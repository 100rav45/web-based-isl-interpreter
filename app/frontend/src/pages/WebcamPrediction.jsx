import { useRef, useState } from "react";
import Webcam from "react-webcam";

import Layout from "../components/Layout/Layout";
import api from "../services/api";
import "./WebcamPrediction.css";
import PredictionCard from "../components/PredictionCard/PredictionCard";

export default function WebcamPrediction() {

    const webcamRef = useRef(null);

    const [prediction, setPrediction] = useState("");

    const [confidence, setConfidence] = useState(0);

    const [countdown, setCountdown] = useState(null);

    const [loading, setLoading] = useState(false);

    const [capturing, setCapturing] = useState(false);

    const [flash, setFlash] = useState(false);

    async function captureFrame() {

        if (capturing) return;

        setPrediction("");
        setConfidence(0);

        setCapturing(true);

        setPrediction("");

        setConfidence(0);

        let time = 4;

        setCountdown(time);

        const timer = setInterval(() => {

            time--;

            setCountdown(time);

            if (time === 0) {

                clearInterval(timer);

                captureNow();

            }

        }, 1000);

    }

    async function captureNow() {

        setCountdown(null);

        setLoading(true);

        setFlash(true);

        setTimeout(() => {

            setFlash(false);

        }, 200);

        const imageSrc = webcamRef.current.getScreenshot();

        const blob = await fetch(imageSrc).then(res => res.blob());

        const formData = new FormData();

        formData.append(
            "file",
            blob,
            "frame.jpg"
        );

        try {

            const response = await api.post(
                "/predict-frame",
                formData
            );

            setPrediction(response.data.prediction);

            setConfidence(response.data.confidence);

        }

        catch(error){

            console.error(error);

        }

        setLoading(false);

        setCapturing(false);

    }

    return (

        <Layout>
            <div className="webcam-page">

                <div className="prediction-card">

                    <h1 className="page-title">
                        Live ISL Recognition
                    </h1>

                    <p className="page-subtitle">
                        Capture a gesture from your webcam and let the AI predict it.
                    </p>

                    <div className="tips-box">
                        <h3>💡Recognition Tips</h3>

                        <ul>
                            <li>  Use good lighting</li>
                            <li>Keep one hand fully visible</li>
                            <li>Use a plain background if possible</li>
                            <li>Center your hand in the frame</li>
                        </ul>
                    </div>

                    <div className="webcam-layout">

                        {/* ================= LEFT PANEL ================= */}

                        <div className="camera-panel">

                            <h2 className="section-title">Live Camera Feed</h2>
                            <div className="webcam-container">

                                <Webcam
                                    ref={webcamRef}
                                    audio={false}
                                    screenshotFormat="image/jpeg"
                                    className="webcam-feed"
                                    videoConstraints={{
                                        width: 1280,
                                        height: 720,
                                        facingMode: "user",
                                    }}
                                />

                                {flash && (
                                    <div className="camera-flash"></div>
                                )}

                                {countdown !== null && (
                                    <div className="countdown-overlay">
                                        {countdown}
                                    </div>
                                )}

                            </div>

                            <div className="status-row">

                                {!capturing && !loading && (
                                    <span className="status ready">
                                        🟢 Camera Ready
                                    </span>
                                )}

                                {capturing && (
                                    <span className="status capture">
                                        📸 Capturing Gesture...
                                    </span>
                                )}

                                {loading && (
                                    <span className="status loading">
                                        🤖 AI Processing...
                                    </span>
                                )}

                            </div>

                            <button
                                className="capture-btn"
                                onClick={captureFrame}
                                disabled={capturing}
                            >

                                {capturing
                                    ? `Capturing in ${countdown}`
                                    : "📸 Capture & Predict"}

                            </button>

                        </div>

                        {/* ================= RIGHT PANEL ================= */}

                        <div className="prediction-panel">
                            <h2 className="section-title">
                                Prediction Result
                            </h2>

                            {(prediction || confidence > 0) ? (

                                
                                <PredictionCard
                                    result={{
                                        prediction,
                                        confidence,
                                        processing_time_ms: 0
                                    }}
                                />

                            ) : (

                                <div className="empty-result">

                                    <div className="empty-icon">
                                        🤟
                                    </div>

                                    <h2>No Prediction Yet</h2>

                                    <p>

                                        Capture a hand gesture to see the AI prediction.

                                    </p>

                                </div>

                            )}

                        </div>

                    </div>

                </div>

            </div>
        </Layout>

    );

}