import axios from 'axios';

const API_URL = import.meta.env.VITE_BACKEND_URL || 'http://localhost:8000';

const fetchCategorySumsForYear = async (year) => {
  const payload = { year: year };
  try {
    const response = await axios.get(`${API_URL}/sums-by-category`, payload);
    console.log("Fetched category sums for year:", response.data.data);
    return response.data.data;
  } catch (error) {
    console.error("Error fetching chart data:", error);
    throw error;
  }
};

const addNewProduct = async (productData) => {
  try {
    const response = await axios.post(`${API_URL}/add-product`, productData);
    return response.data;
  } catch (error) {
    console.error("Error adding new product:", error);
    throw error;
  }
};

const updateProduct = async (productId, updatedData) => {
  try {
    const response = await axios.put(`${API_URL}/update-product/${productId}`, updatedData);
    return response.data;
  } catch (error) {
    console.error("Error updating product:", error);
    throw error;
  }
};

const getTenRecentlyAddedProducts = async () => {
  try {
    const response = await axios.get(`${API_URL}`);
    const tenProducts = response.data;
    return tenProducts.data
    
  } catch (error) {
    console.error("Error fetching ten recently added products:", error);
    throw error;
  }
};

const deleteProduct = async (productId) => {
  try {
    const response = await axios.delete(`${API_URL}/delete-product/${productId}`);
    return response.data;
  } catch (error) {
    console.error("Error deleting product:", error);
    throw error;
  }
};

export default {
  fetchCategorySumsForYear,
  addNewProduct,
  updateProduct,
  getTenRecentlyAddedProducts,
  deleteProduct
};