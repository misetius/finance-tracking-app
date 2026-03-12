const productForm = (props) => {
    return (
        <div class="container">
            <h3>Add a new product</h3>
        <form onSubmit={props.addProduct} >
            <div>
                <label htmlFor="name">Product Name:</label>
                <input type="text" id="name" name="name" required onChange={props.onNameChange} />
            </div>
            <div>
                <label htmlFor="price">Price:</label>
                <input type="number" id="price" name="price" step="0.01" required onChange={props.onPriceChange} />
            </div>
            <div>
                <label htmlFor="category">Category:</label>
                <select id="category" name="category" required onChange={props.onCategoryChange}>
                    <option value="">Select a category</option>
                    <option value="food">Food</option>
                    <option value="drinks">Drinks</option>
                    <option value="entertainment">Entertainment</option>
                    <option value="apartment">Apartment (rent, utilities)</option>
                    <option value="electronics">Electronics</option>
                    <option value="sports">Sports</option>
                    <option value="other">Other</option>
                </select>
            </div>
            <input type="submit" id="submit" value="Add Product" />
        </form>
        </div>

    );
}

export default productForm;