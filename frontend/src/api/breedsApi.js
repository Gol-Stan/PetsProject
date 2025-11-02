import axios from 'axios';


const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || '/api';

export const getBreeds = async () => {
    const response = await axios.get(`${API_BASE_URL}/breeds/`);
    return response.data;
};