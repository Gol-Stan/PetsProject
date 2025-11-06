// src/api/authApi.js
import axios from "axios";

const API_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

export const registerUser = async ({ name, email, password }) => {
    try {
        const response = await axios.post(`${API_URL}/auth/register`, {
            name: name,
            email: email,
            password: password,
        }, {
            headers: {
                "Content-Type": "application/json",
            },
        });
        return response.data;
    } catch (error) {
        console.error("Registration error:", error);
        console.error("Error response:", error.response?.data);
        throw error.response?.data || { detail: "Registration failed" };
    }
};

export const loginUser = async ({ email, password }) => {
    try {
        const params = new URLSearchParams();
        params.append('username', email);
        params.append('password', password);

        const response = await axios.post(`${API_URL}/auth/login`, params, {
            headers: {
                "Content-Type": "application/x-www-form-urlencoded",
            },
        });
        return response.data;
    } catch (error) {
        console.error("Login error:", error);
        console.error("Error response:", error.response?.data);
        throw error.response?.data || { detail: "Login failed" };
    }
};

export const getCurrentUser = () => {
    return localStorage.getItem("username");
};