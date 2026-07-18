import { useState } from "react";

import api from "../services/api";

import Layout from "../components/Layout/Layout";

import ImageUploader from "../components/ImageUploader/ImageUploader";

import PredictionCard from "../components/PredictionCard/PredictionCard";

import Loader from "../components/Loader/Loader";

import "./ImagePrediction.css";

export default function ImagePrediction() {

    const [image, setImage] = useState(null);

    const [result, setResult] = useState(null);

    const [loading, setLoading] = useState(false);

    async function handlePrediction() {

        if (!image) return;

        setResult(null);
        
        setLoading(true);

        const formData = new FormData();

        formData.append("file", image);

        try {

            const response = await api.post(

                "/predict-image",

                formData

            );

            setResult(response.data);

        }

        catch(error){

            console.error(error);

        }

        finally{

            setLoading(false);

        }

    }

    return (

        <Layout>

            <div className="predict-container">
                

                <div className="page-header">

                    <div className="page-header">

                        <h1>
                            Image Prediction
                        </h1>

                        <p>
                            Upload a clear image of an Indian Sign Language hand gesture.
                            Our AI model will analyze the hand landmarks and predict the
                            corresponding gesture with confidence.
                        </p>

                    </div>

                    <p>
                        Upload an image to
                        receive an AI-powered prediction.
                    </p>

                </div>

               <ImageUploader
                    image={image}
                    setImage={setImage}
                    disabled={loading}
                />

                <button
                    className="predict-btn"
                    onClick={handlePrediction}
                    disabled={!image || loading}
                >
                    {loading ? "Predicting..." : "Predict Gesture"}
                </button>

                {
                    loading

                    ? <Loader />

                    : <PredictionCard
                        result={result}
                    />
                }

            </div>

        </Layout>

    );

}