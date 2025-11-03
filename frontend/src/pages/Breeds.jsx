// src/pages/Breeds.jsx
import { useEffect, useState } from "react";
import { getBreeds } from "../api/breedsApi";

function BreedCard({ breed, onOpen }) {
    return (
        <div
            className="bg-white rounded-lg shadow-md p-4 text-center hover:shadow-lg transition cursor-pointer"
            onClick={() => onOpen(breed)}
        >
            <img
                src={`http://localhost:8000${breed.img}`}
                alt={breed.name}
                className="w-48 h-48 object-cover mx-auto rounded mb-3"
            />
            <h3 className="text-xl font-semibold text-gray-800">{breed.name}</h3>
        </div>
    );
}

function BreedModal({ breed, onClose }) {
    if (!breed) return null;

    const handleBackdropClick = (e) => {
        if (e.target === e.currentTarget) onClose();
    };

    return (
        <div
            className="fixed inset-0 bg-black bg-opacity-40 flex items-center justify-center z-50"
            onClick={handleBackdropClick}
        >
            <div className="bg-orange-100 rounded-lg shadow-lg p-6 max-w-lg w-full max-h-[90vh] overflow-y-auto relative">
                <button
                    onClick={onClose}
                    className="absolute top-3 right-3 text-gray-800 hover:text-black text-lg"
                >
                    ✕
                </button>

                <img
                    src={`http://localhost:8000${breed.img}`}
                    alt={breed.name}
                    className="w-64 h-64 object-cover mx-auto rounded mb-4"
                />
                <h3 className="text-2xl font-bold mb-3 text-gray-800 text-center">
                    {breed.name}
                </h3>
                <p className="text-gray-700 font-semiboldbold leading-relaxed whitespace-pre-line">
                    {breed.description}
                </p>
            </div>
        </div>
    );
}

export default function Breeds() {
    const [breeds, setBreeds] = useState([]);
    const [selectedBreed, setSelectedBreed] = useState(null);

    useEffect(() => {
        getBreeds().then(setBreeds).catch(console.error);
    }, []);

    return (
        <div className="max-w-6xl mx-auto px-4 py-8">
            <h2 className="text-3xl font-bold mb-6 text-center text-gray-800">
                Dog Breeds
            </h2>

            <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
                {breeds.map((breed) => (
                    <BreedCard key={breed.id} breed={breed} onOpen={setSelectedBreed} />
                ))}
            </div>

            <BreedModal breed={selectedBreed} onClose={() => setSelectedBreed(null)} />
        </div>
    );
}
