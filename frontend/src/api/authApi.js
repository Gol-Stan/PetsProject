// src/api/authApi.js
import axios from "axios";

const API_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

// Создаем экземпляр axios с базовой конфигурацией
const api = axios.create({
    baseURL: API_URL,
});

// Добавляем интерцептор для автоматической подстановки токена
api.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem("access_token");
        if (token) {
            config.headers.Authorization = `Bearer ${token}`;
        }
        return config;
    },
    (error) => {
        return Promise.reject(error);
    }
);

export const registerUser = async ({ email, password }) => {
    try {
        const response = await api.post("/auth/register", {
            email,
            password,
        });
        return response.data;
    } catch (error) {
        console.error("Registration error:", error);
        throw error.response?.data || { detail: "Registration failed" };
    }
};

export const loginUser = async ({ email, password }) => {
    try {
        const formData = new FormData();
        formData.append("username", email);
        formData.append("password", password);

        const response = await api.post("/auth/login", formData, {
            headers: {
                "Content-Type": "application/x-www-form-urlencoded",
            },
        });
        return response.data;
    } catch (error) {
        console.error("Login error:", error);
        throw error.response?.data || { detail: "Login failed" };
    }
};

// Функция для проверки токена
export const verifyToken = async () => {
    try {
        const token = localStorage.getItem("access_token");
        if (!token) return false;

        // Здесь можно добавить запрос для проверки токена
        // Например: await api.get("/auth/me");
        return true;
    } catch (error) {
        localStorage.removeItem("access_token");
        localStorage.removeItem("username");
        return false;
    }
};

// Функция для получения текущего пользователя
export const getCurrentUser = () => {
    return localStorage.getItem("username");
};