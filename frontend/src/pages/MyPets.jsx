// src/pages/MyPets.jsx
import { useState, useEffect } from "react";
import { getCurrentUser } from "../api/authApi";

export default function MyPets() {
    const [user, setUser] = useState("");

    useEffect(() => {
        const currentUser = getCurrentUser();
        setUser(currentUser || "");
    }, []);

    return (
        <div className="max-w-4xl mx-auto">
            <h2 className="text-3xl font-bold mb-6 text-center text-gray-800">My Pets</h2>

            {user ? (
                <div className="bg-white rounded-lg shadow-md p-6">
                    <p className="text-lg mb-4">
                        Welcome, <span className="font-semibold text-orange-600">{user}</span>!
                    </p>
                    <p className="text-gray-600">
                        This is your personal pets management page.
                    </p>
                </div>
            ) : (
                <div className="bg-yellow-50 border border-yellow-200 rounded-lg p-6 text-center">
                    <p className="text-yellow-800 mb-4">
                        Please log in to view and manage your pets.
                    </p>
                    <p className="text-sm text-yellow-600">
                        Use the Login/Register button in the header.
                    </p>
                </div>
            )}
        </div>
    );
}