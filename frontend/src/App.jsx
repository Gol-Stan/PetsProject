import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

export default function App() {
    return (
        <div className="flex flex-col items-center justify-center min-h-screen text-center">
            <h1 className="text-4xl font-bold text-blue-600 mb-4">
                Добро пожаловать на сайт о животных 🐾
            </h1>
            <p className="text-lg text-gray-700 max-w-md">
                Здесь вы сможете создавать карточки питомцев, делиться историями и находить новых друзей.
            </p>
            <button className="mt-8 px-6 py-3 bg-blue-600 hover:bg-blue-700 text-white font-semibold rounded-lg transition">
                Начать
            </button>
        </div>
    );
}
