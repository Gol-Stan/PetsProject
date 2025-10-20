import { useState } from "react";
import logo from "../assets/logo.png";
import background from "../assets/background.jpg";

export default function Header() {
    const [user, setUser] = useState("");
    const [name, setName] = useState("");
    const [password, setPassword] = useState("");
    const [showLogin, setShowLogin] = useState(false);

    const handleLogin = (e) => {
        e.preventDefault();
        if (name.trim() && password.trim()) {
            setUser(name);
            setShowLogin(false);
            setName("");
            setPassword("");
        }
    };

    const handleLogout = () => setUser("");

    return (
        <header
            className="relative flex items-center h-36 bg-cover bg-[center_75%] shadow-md"
            style={{
                backgroundImage: `linear-gradient(rgba(255,255,255,0.1), rgba(255,255,255,0.1)), url(${background})`,
            }}
        >
            <div className="w-full flex justify-between items-center px-12 relative">

                <div className="flex items-center gap-3">
                    <img src={logo} alt="PetZone Logo" className="w-12 h-12 object-contain" />
                    <h1 className="text-3xl font-bold text-gray-800">PetWorld</h1>
                </div>


                <div className="relative">
                    {user ? (
                        <div className="flex items-center gap-4">
                            <p className="text-white">
                                Good to see you, <span className="font-semibold">{user}</span>!
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
                                <div className="absolute right-0 mt-3 bg-white border border-gray-200 rounded-lg shadow-lg p-4 w-64 animate-fadeIn">
                                    <form onSubmit={handleLogin} className="flex flex-col gap-3">
                                        <input
                                            type="email"
                                            placeholder="Email"
                                            value={name}
                                            onChange={(e) => setName(e.target.value)}
                                            className="border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-orange-600"
                                        />
                                        <input
                                            type="password"
                                            placeholder="Password"
                                            value={password}
                                            onChange={(e) => setPassword(e.target.value)}
                                            className="border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-orange-600"
                                        />
                                        <button
                                            type="submit"
                                            className="bg-orange-400 text-white px-3 py-2 rounded hover:bg-orange-600 transition"
                                        >
                                            Login
                                        </button>
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
