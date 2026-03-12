import { use, useEffect, useState } from 'react'
import chartservice from '../services/chart_data'
import ProductForm from '../components/add_product_form'
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js';
import { Pie } from 'react-chartjs-2';
import Product from '../components/ten_recently_added_products';
ChartJS.register(ArcElement, Tooltip, Legend);


const App = () => {
const [categorySpending, setCategorySpending] = useState([]); 
const [category, setCategory] = useState('');
const [price, setPrice] = useState('');
const [name, setName] = useState('');
const [recentProducts, setRecentProducts] = useState([]);


useEffect(() => {
  const date = new Date();
  const year = date.getFullYear();
  chartservice.fetchCategorySumsForYear(year)
    .then(data => {
      setCategorySpending(data);
    })
    .catch(error => {
      console.error("Error fetching category spending data:", error);
    });
  chartservice.getTenRecentlyAddedProducts()
    .then(data => {
      setRecentProducts(data);
    })
    .catch(error => {
      console.error("Error fetching recently added products:", error);
    });
}, []);



const datasetsForCategories = {
  labels: categorySpending.map(item => item.category),
  datasets: [
  {
    labels: "Category Spending",
    data: categorySpending.map(item => item.total_price),
    backgroundColor: [
  'rgba(255, 107, 107, 0.2)',  
  'rgba(30, 58, 138, 0.2)',    
  'rgba(255, 159, 28, 0.2)',   
  'rgba(97, 160, 255, 0.2)',   
  'rgba(139, 0, 255, 0.2)',    
  'rgba(30, 30, 30, 0.2)'      
],
borderColor: [
  'rgba(255, 107, 107, 1)',   
  'rgba(30, 58, 138, 1)',      
  'rgba(255, 159, 28, 1)',     
  'rgba(97, 160, 255, 1)',     
  'rgba(139, 0, 255, 1)',      
  'rgba(30, 30, 30, 1)'        
],
    borderWidth: 1,
  },
],
};

const onNameChange = (event) => {
  setName(event.target.value);
}

const onPriceChange = (event) => {
  setPrice(event.target.value);
}

const onCategoryChange = (event) => {
  setCategory(event.target.value);
}

const addProduct = async (event) => {
  // event.preventDefault();
  const newProduct = {
    category: category,
    product: name,
    price: parseFloat(price)
  };
  try {
    await chartservice.addNewProduct(newProduct);
    console.log("Product added successfully:", newProduct);
    
  }
  catch (error) {
    console.error("Error adding product:", error);
  }
}
  
const deleteProduct = async (productId) => {
    try {
      await chartservice.deleteProduct(productId);
      setRecentProducts(recentProducts.filter(product => product.id !== productId));
    } catch (error) {
      console.error("Error deleting product:", error);
    }
  };



return(
  <div style={{ display: "flex", justifyContent: "center" }}>
   <div style={{ width: "400px" }}> 
    <h1>Finance Tracking App</h1>
    <h2>Spending by Category For the Year</h2>
    <Pie  data={datasetsForCategories} />
    <ProductForm addProduct={addProduct} onNameChange={onNameChange} onPriceChange={onPriceChange} onCategoryChange={onCategoryChange} />
    <h3>10 Recently Added Products (Click to Delete)</h3>
      {recentProducts.map(product => (
        <Product key={product.id} product={product} deleteProduct={() => deleteProduct(product.id)} />
      ))}
  </div>
  </div>
)
}




export default App