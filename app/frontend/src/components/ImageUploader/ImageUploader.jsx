import { useRef, useState } from "react";
import "./ImageUploader.css";

export default function ImageUploader({ image, setImage }) {

    const inputRef = useRef(null);

    const [dragActive, setDragActive] = useState(false);

    function handleFile(file) {

        if (!file) return;

        setImage(file);

    }

    function handleChange(e) {

        handleFile(e.target.files[0]);

    }

    function handleDrop(e) {

        e.preventDefault();

        setDragActive(false);

        handleFile(e.dataTransfer.files[0]);

    }

    function handleDragOver(e) {

        e.preventDefault();

        setDragActive(true);

    }

    function handleDragLeave(e) {

        e.preventDefault();

        setDragActive(false);

    }

    return (

        <div className="uploader-container">

            <div
                className={`upload-area ${dragActive ? "drag-active" : ""}`}
                onClick={() => inputRef.current.click()}
                onDrop={handleDrop}
                onDragOver={handleDragOver}
                onDragLeave={handleDragLeave}
            >

                {

                    image ?

                    <>

                        <img
                            src={URL.createObjectURL(image)}
                            alt="Preview"
                            className="preview"
                        />

                        <p className="file-name">

                            {image.name}

                        </p>

                        <button
                            type="button"
                            className="change-image-btn"
                            onClick={(e) => {

                                e.stopPropagation();

                                inputRef.current.click();

                            }}
                        >

                            Change Image

                        </button>

                    </>

                    :

                    <>

                        <div className="upload-icon">

                            📷

                        </div>

                        <h2>

                            Drop your ISL image here

                        </h2>

                        <p>

                            Supported formats: JPG • JPEG • PNG

                        </p>

                        <span className="upload-divider">

                            — OR —

                        </span>

                        <button
                            type="button"
                            className="browse-btn"
                            onClick={(e) => {

                                e.stopPropagation();

                                inputRef.current.click();

                            }}
                        >

                            Browse Files

                        </button>

                    </>

                }

            </div>

            <input

                ref={inputRef}

                type="file"

                accept="image/*"

                hidden

                onChange={handleChange}

            />

        </div>

    );

}