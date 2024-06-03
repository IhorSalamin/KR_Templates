import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:5000/api';

export const getCars = () => axios.get(`${API_BASE_URL}/cars`);
export const getClients = () => axios.get(`${API_BASE_URL}/user`);
export const createClient = (clientData) => axios.post(`${API_BASE_URL}/user`, clientData);
export const getBookings = () => axios.get(`${API_BASE_URL}/bookings`);
export const createBooking = (bookingData) => axios.post(`${API_BASE_URL}/booking`, bookingData);
export const addCar = (carData) => axios.post(`${API_BASE_URL}/car`, carData);
// Додайте інші необхідні запити до API
