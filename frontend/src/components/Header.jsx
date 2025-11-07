// src/components/Header.jsx
import { useState, useEffect } from "react";
import { Link, useNavigate } from "react-router-dom";
import { loginUser, getCurrentUser } from "../api/authApi";
import logo from "../assets/logo.png";
import background from "../assets/background.jpg";

export default function Header() {
    const [user, setUser] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [showLogin, setShowLogin] = useState(false);
    const [error, setError] = useState("");
    const navigate = useNavigate();

    // Загружаем пользователя при загрузке компонента
    useEffect(() => {
        const currentUser = getCurrentUser();
        if (currentUser) {
            setUser(currentUser);
        }
    }, []);

    const handleLogin = async (e) => {
        e.preventDefault();
        try {
            const data = await loginUser({ email, password });
            localStorage.setItem("access_token", data.access_token);

            localStorage.setItem("username", data.name || email);
            setUser(data.name || email);

            setShowLogin(false);
            setEmail("");
            setPassword("");
            setError("");
        } catch (err) {
            setError(err.detail || "Login failed");
        }
    };

    const handleLogout = () => {
        localStorage.removeItem("access_token");
        localStorage.removeItem("username");
        setUser("");
    };

    const handleRegisterClick = () => {
        setShowLogin(false); // Закрываем попап логина
        navigate("/register"); // Переходим на страницу регистрации
    };

    return (
        <header
            className="relative flex items-center h-36 bg-cover bg-[center_75%] shadow-md"
            style={{
                backgroundImage: `linear-gradient(rgba(255,255,255,0.1), rgba(255,255,255,0.1)), url(${background})`,
            }}
        >
            <div className="w-full flex justify-between items-center px-12 relative">
                <Link to="/">
                    <div className="flex items-center gap-3">
                        <img src={logo} alt="PetZone Logo" className="w-12 h-12 object-contain" />
                        <h1 className="text-3xl font-bold text-gray-800">PetWorld</h1>
                    </div>
                </Link>

                <div className="relative">
                    {user ? (
                        <div className="flex items-center gap-4">
                            <p className="text-white bg-black bg-opacity-50 px-3 py-1 rounded">
                                Welcome, <span className="font-semibold">{user}</span>!
                            </p>
                            <button
                                onClick={handleLogout}
                                className="bg-orange-400 text-white px-4 py-2 rounded hover:bg-orange-600 transition"
                            >
                                Logout
                            </button>
                        </div>
                    ) : (
                        <>
                            <button
                                onClick={() => setShowLogin((prev) => !prev)}
                                className="bg-orange-400 text-white px-4 py-2 rounded hover:bg-orange-600 transition"
                            >
                                Login / Register
                            </button>

                            {showLogin && (
                                <div className="absolute right-0 mt-3 bg-white border border-gray-200 rounded-lg shadow-lg p-4 w-80 z-50">
                                    <form onSubmit={handleLogin} className="flex flex-col gap-3">
                                        <h3 className="text-lg font-semibold text-center">Login</h3>

                                        <input
                                            type="email"
                                            placeholder="Email"
                                            value={email}
                                            onChange={(e) => setEmail(e.target.value)}
                                            className="border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-orange-600"
                                            required
                                        />
                                        <input
                                            type="password"
                                            placeholder="Password"
                                            value={password}
                                            onChange={(e) => setPassword(e.target.value)}
                                            className="border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-orange-600"
                                            required
                                        />

                                        <button
                                            type="submit"
                                            className="bg-orange-400 text-white px-3 py-2 rounded hover:bg-orange-600 transition"
                                        >
                                            Login
                                        </button>

                                        {/* Кнопка Register которая ведет на страницу регистрации */}
                                        <button
                                            type="button"
                                            onClick={handleRegisterClick}
                                            className="text-center bg-gray-200 text-gray-800 px-3 py-2 rounded hover:bg-gray-300 transition"
                                        >
                                            Register
                                        </button>

                                        {error && <p className="text-sm text-red-600 text-center">{error}</p>}
                                    </form>
                                </div>
                            )}
                        </>
                    )}
                </div>
            </div>
        </header>
    );
}