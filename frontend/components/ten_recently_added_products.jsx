const Product = (props) => {
    return (
        <div>
        <div>
        <p>
            <button className="deleteButton" onClick={props.deleteProduct}><strong>{props.product.product}</strong> - ${props.product.price.toFixed(2)} ({props.product.category})</button>
            </p>

        </div>
        </div>
    );
};

export default Product;