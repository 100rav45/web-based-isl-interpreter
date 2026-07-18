import { Routes, Route } from "react-router-dom";

import Home from "./pages/Home";
import ImagePrediction from "./pages/ImagePrediction";
import About from "./pages/About";
import WebcamPrediction from "./pages/WebcamPrediction";

function App() {

    return (

        <Routes>

            <Route
                path="/"
                element={<Home />}
            />

            <Route
                path="/predict"
                element={<ImagePrediction />}
            />

            <Route
                path="/about"
                element={<About />}
            />

            <Route
                path="/webcam"
                element={<WebcamPrediction />}
            />

        </Routes>

    );

}

export default App;