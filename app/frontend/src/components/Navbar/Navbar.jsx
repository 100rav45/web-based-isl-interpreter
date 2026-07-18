import "./Navbar.css";
import { NavLink } from "react-router-dom";
import logo from "../../assets/logo.png";

export default function Navbar() {
    return (
        <nav className="navbar">

            <div className="logo">

                <img
                    src={logo}
                    alt="ISL Interpreter Logo"
                    className="logo-image"
                />

                <div className="logo-text">

                    <span className="logo-title">
                        ISL Interpreter
                    </span>

                    <span className="logo-subtitle">
                        Real-Time Sign Recognition
                    </span>

                </div>

            </div>

            <div className="nav-links">

                <NavLink to="/">
                    Home
                </NavLink>

                <NavLink to="/predict">
                    Predict
                </NavLink>

                <NavLink to="/webcam">
                    Webcam
                </NavLink>

                <NavLink to="/about">
                    About
                </NavLink>

            </div>

        </nav>
    );
}