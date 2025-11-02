import { useEffect, useState } from "react";
import { getBreeds } from "../api/breedsApi";

function BreedCard({ breed }) {
    return (
        <div className="bg-white rounded-lg shadow-md p-4 text-center hover:shadow-xl transition">
            <img
                // Use Vite environment variable or relative path
                src={breed.img ? `${import.meta.env.VITE_API_BASE_URL || ''}${breed.img}` : '/placeholder-image.jpg'}
                alt={breed.name}
                className="w-40 h-40 object-cover mx-auto rounded"
                onError={(e) => {
                    e.target.src = '/placeholder-image.jpg'; // Fallback image
                }}
            />
            <h3 className="text-xl font-semibold mt-2">{breed.name}</h3>
            <p className="text-gray-600 text-sm mt-1">
                {breed.description ? breed.description.slice(0, 100) + '...' : 'No description available'}
            </p>
        </div>
    );
}

export default function Breeds() {
    const [breeds, setBreeds] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchBreeds = async () => {
            try {
                setLoading(true);
                const breedsData = await getBreeds();
                setBreeds(breedsData);
                setError(null);
            } catch (err) {
                setError('Failed to load breeds. Please try again later.');
                console.error('Error fetching breeds:', err);
            } finally {
                setLoading(false);
            }
        };

        fetchBreeds();
    }, []);

    if (loading) {
        return (
            <div className="max-w-6xl mx-auto px-4 py-8">
                <div className="text-center">Loading breeds...</div>
            </div>
        );
    }

    if (error) {
        return (
            <div className="max-w-6xl mx-auto px-4 py-8">
                <div className="text-center text-red-500">{error}</div>
            </div>
        );
    }

    return (
        <div className="max-w-6xl mx-auto px-4 py-8">
            <h2 className="text-3xl font-bold mb-6 text-center text-gray-800">Dog Breeds</h2>
            {breeds.length === 0 ? (
                <div className="text-center text-gray-500">No breeds found.</div>
            ) : (
                <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
                    {breeds.map((breed) => (
                        <BreedCard key={breed.id} breed={breed} />
                    ))}
                </div>
            )}
        </div>
    );
}