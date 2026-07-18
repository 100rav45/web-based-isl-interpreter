import Layout from "../components/Layout/Layout";
import "./About.css";

export default function About() {

    return (

        <Layout>

            <div className="about-page">

                <div className="about-card">

                    <h1 className="about-title">
                        ℹ️ About ISL Interpreter
                    </h1>

                    <p className="about-subtitle">
                        A Real-Time Indian Sign Language Recognition System developed
                        using Artificial Intelligence and Computer Vision.
                    </p>

                    {/* Project Overview */}

                    <section className="about-section">

                        <h2>📖 Project Overview</h2>

                        <p>

                            ISL Interpreter is a web-based application that recognizes
                            Indian Sign Language gestures from both uploaded images and
                            live webcam input. The system uses MediaPipe for extracting
                            hand landmarks and a Random Forest classifier to predict the
                            corresponding gesture in real time.

                        </p>

                    </section>

                    {/* Features */}

                    <section className="about-section">

                        <h2>🚀 Features</h2>

                        <div className="feature-grid">

                            <div className="feature-box">
                                📷 Image Recognition
                            </div>

                            <div className="feature-box">
                                🎥 Live Webcam Recognition
                            </div>

                            <div className="feature-box">
                                🤖 Random Forest Classifier
                            </div>

                            <div className="feature-box">
                                🖐 MediaPipe Hand Tracking
                            </div>

                            <div className="feature-box">
                                ⚡ FastAPI Backend
                            </div>

                            <div className="feature-box">
                                ⚛ React Frontend
                            </div>

                        </div>

                    </section>

                    {/* Technology */}

                    <section className="about-section">

                        <h2>🛠 Technology Stack</h2>

                        <div className="tech-grid">

                            <div>React</div>
                            <div>FastAPI</div>
                            <div>Python</div>
                            <div>MediaPipe</div>
                            <div>OpenCV</div>
                            <div>Random Forest</div>

                        </div>

                    </section>

                    {/* Workflow */}

                    <section className="about-section">

                        <h2>🔄 System Workflow</h2>

                        <div className="workflow">

                            <div className="workflow-step">
                                📷 Image / Webcam
                            </div>

                            <div className="workflow-arrow">↓</div>

                            <div className="workflow-step">
                                🖐 Hand Landmark Detection
                            </div>

                            <div className="workflow-arrow">↓</div>

                            <div className="workflow-step">
                                📊 Feature Extraction
                            </div>

                            <div className="workflow-arrow">↓</div>

                            <div className="workflow-step">
                                🌳 Random Forest Prediction
                            </div>

                            <div className="workflow-arrow">↓</div>

                            <div className="workflow-step">
                                ✅ Display Result
                            </div>

                        </div>

                    </section>

                    {/* Dataset */}

                    <section className="about-section">

                        <h2>📊 Dataset</h2>

                        <div className="stats-grid">

                            <div className="stat-card">

                                <h3>36</h3>

                                <p>Classes</p>

                            </div>

                            <div className="stat-card">

                                <h3>41,815</h3>

                                <p>Training Samples</p>

                            </div>

                            <div className="stat-card">

                                <h3>99.93%</h3>

                                <p>Model Accuracy</p>

                            </div>

                        </div>

                    </section>

                    {/* Footer */}

                    <section className="about-footer">

                        <h3>🎓 MCA Major Project</h3>

                        <p>

                            Developed using React, FastAPI, MediaPipe,
                            OpenCV and Random Forest.

                        </p>

                    </section>

                </div>

            </div>

        </Layout>

    );

}