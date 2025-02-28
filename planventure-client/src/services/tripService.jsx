import { api } from './api';

export const tripService = {
  getAllTrips: async () => {
    try {
      console.log('Fetching trips with auth token:', localStorage.getItem('token')); // Debug log
      const response = await api.get('/api/trips');
      console.log('Trips response:', response); // Debug log
      return response;
    } catch (error) {
      console.error('Error in getAllTrips:', error); // Debug log
      if (error.message.includes('Session expired')) {
        // Handle session expiration specifically
        return { trips: [] };
      }
      throw error;
    }
  },

  createTrip: async (tripData) => {
    try {
      const response = await api.post('/api/trips', tripData);
      return response.data;
    } catch (error) {
      throw new Error(error.response?.data?.message || 'Failed to create trip');
    }
  },

  getTrip: async (tripId) => {
    try {
      const response = await api.get(`/api/trips/${tripId}`);
      return response.data;
    } catch (error) {
      throw new Error(error.response?.data?.message || 'Failed to fetch trip');
    }
  }
};
