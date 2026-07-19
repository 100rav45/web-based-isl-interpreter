import "./Navbar.css";
import { NavLink } from "react-router-dom";
import { useState } from "react";
import logo from "../../assets/logo.png";

export default function Navbar() {

    const [menuOpen, setMenuOpen] = useState(false);

    return (
        <nav className="navbar">

            <NavLink
                to="/"
                className="logo"
                onClick={() => setMenuOpen(false)}
            >

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

            </NavLink>

            <div
                className={`nav-links ${menuOpen ? "open" : ""}`}
            >

                <NavLink
                    to="/"
                    onClick={() => setMenuOpen(false)}
                >
                    Home
                </NavLink>

                <NavLink
                    to="/predict"
                    onClick={() => setMenuOpen(false)}
                >
                    Predict
                </NavLink>

                <NavLink
                    to="/webcam"
                    onClick={() => setMenuOpen(false)}
                >
                    Webcam
                </NavLink>

                <NavLink
                    to="/about"
                    onClick={() => setMenuOpen(false)}
                >
                    About
                </NavLink>

            </div>

            <div
                className="menu-icon"
                onClick={() => setMenuOpen(!menuOpen)}
            >
                ☰
            </div>

        </nav>
    );
}