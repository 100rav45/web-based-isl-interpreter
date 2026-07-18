import { useNavigate } from "react-router-dom";
import Layout from "../components/Layout/Layout";
import FeatureCard from "../components/FeatureCard/FeatureCard";
import logo from "../assets/logo.png";
import "./Home.css";

export default function Home() {

    const navigate = useNavigate();

    return (

        <Layout>

            {/* ================= HERO ================= */}

            <section className="hero">

                <div className="hero-left">

                    <img
                        src={logo}
                        alt="ISL Interpreter"
                        className="hero-logo"
                    />

                    <span className="hero-badge">
                        AI Powered Recognition System
                    </span>

                    <h1>
                        ISL Interpreter
                    </h1>

                    <h2>
                        Real-Time Indian Sign Language Recognition
                    </h2>

                    <p>

                        ISL Interpreter is an AI-powered web application
                        that recognizes Indian Sign Language gestures using
                        MediaPipe hand landmark detection and a Random Forest
                        Machine Learning model. The application supports both
                        image-based and real-time webcam prediction through a
                        modern web interface.

                    </p>

                    <div className="hero-buttons">

                        <button
                            onClick={() => navigate("/predict")}
                        >
                            📷 Upload Image
                        </button>

                        <button
                            className="secondary-btn"
                            onClick={() => navigate("/webcam")}
                        >
                            🎥 Live Webcam
                        </button>

                    </div>

                </div>

                <div className="hero-right">

                    <div className="hero-stats">

                        <div className="stat-card">

                            <h2>36</h2>

                            <p>Classes</p>

                        </div>

                        <div className="stat-card">

                            <h2>41,815</h2>

                            <p>Dataset Samples</p>

                        </div>

                        <div className="stat-card">

                            <h2>99.93%</h2>

                            <p>Accuracy</p>

                        </div>

                        <div className="stat-card">

                            <h2>&lt;100ms</h2>

                            <p>Prediction</p>

                        </div>

                    </div>

                </div>

            </section>

            {/* ================= FEATURES ================= */}

            <section className="features-section">

                <h2 className="section-title">

                    Why Choose ISL Interpreter?

                </h2>

                <p className="section-subtitle">

                    Powerful AI technologies combined to deliver fast and
                    accurate Indian Sign Language recognition.

                </p>

                <div className="features">

                    <FeatureCard
                        icon="📷"
                        title="Image Prediction"
                        description="Upload gesture images for accurate sign recognition."
                    />

                    <FeatureCard
                        icon="🎥"
                        title="Live Webcam"
                        description="Predict gestures instantly using your webcam."
                    />

                    <FeatureCard
                        icon="🤖"
                        title="AI Recognition"
                        description="MediaPipe hand landmarks with Random Forest classification."
                    />

                    <FeatureCard
                        icon="⚡"
                        title="Real-Time"
                        description="Fast predictions with an optimized recognition pipeline."
                    />

                </div>

            </section>

            {/* ================= TECHNOLOGY STACK ================= */}

            <section className="tech-stack">

                <h2 className="section-title">
                    Technology Stack
                </h2>

                <p className="section-subtitle">
                    Built using modern web technologies and machine learning
                    frameworks for accurate and real-time sign language recognition.
                </p>

                <div className="tech-grid">

                    <div className="tech-card">⚛️ React</div>

                    <div className="tech-card">⚡ FastAPI</div>

                    <div className="tech-card">🐍 Python</div>

                    <div className="tech-card">🖐️ MediaPipe</div>

                    <div className="tech-card">📷 OpenCV</div>

                    <div className="tech-card">🌲 Random Forest</div>

                </div>

            </section>

            {/* ================= HOW IT WORKS ================= */}

            <section className="workflow">

                <h2 className="section-title">
                    How It Works
                </h2>

                <p className="section-subtitle">
                    A simple four-step pipeline converts Indian Sign Language gestures
                    into readable text.
                </p>

                <div className="workflow-container">

                    <div className="workflow-step">

                        <div className="step-number">1</div>

                        <h3>Capture</h3>

                        <p>
                            Upload an image or use the live webcam.
                        </p>

                    </div>

                    <div className="workflow-arrow">→</div>

                    <div className="workflow-step">

                        <div className="step-number">2</div>

                        <h3>Detect</h3>

                        <p>
                            MediaPipe extracts 21 hand landmarks.
                        </p>

                    </div>

                    <div className="workflow-arrow">→</div>

                    <div className="workflow-step">

                        <div className="step-number">3</div>

                        <h3>Predict</h3>

                        <p>
                            Random Forest classifies the gesture.
                        </p>

                    </div>

                    <div className="workflow-arrow">→</div>

                    <div className="workflow-step">

                        <div className="step-number">4</div>

                        <h3>Display</h3>

                        <p>
                            The recognized sign is shown as text.
                        </p>

                    </div>

                </div>

            </section>

            <footer className="footer">

                <h2>ISL Interpreter</h2>

                <p>

                    A Real-Time Indian Sign Language Recognition System
                    developed using React, FastAPI, MediaPipe,
                    OpenCV and Random Forest.

                </p>

                <div className="footer-line"></div>

                <span>

                    © 2026 MCA Major Project • MAKAUT

                </span>

            </footer>

 

        </Layout>

    );

}