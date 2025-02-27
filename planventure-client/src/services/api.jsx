const BASE_URL = import.meta.env.BASE_API_URL || 'http://localhost:5000';

const handleResponse = async (response) => {
  const data = await response.json();
  if (!response.ok) {
    throw new Error(data.error || 'Request failed');
  }
  return data;
};

export const api = {
  // General purpose methods
  get: async (endpoint) => {
    const response = await fetch(`${BASE_URL}${endpoint}`);
    return handleResponse(response);
  },
  
  post: async (endpoint, data) => {
    const response = await fetch(`${BASE_URL}${endpoint}`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    });
    return handleResponse(response);
  },

  // Auth specific methods
  auth: {
    login: async (credentials) => {
      return api.post('/auth/login', credentials);
    },

    register: async (userData) => {
      return api.post('/auth/register', userData);
    }
  }
};

export default api;