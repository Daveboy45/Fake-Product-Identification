// api/static/script.js
window.onload = function() {
    fetch('/api/products')
        .then(response => response.json())
        .then(data => {
            const resultDiv = document.getElementById('result');
            data.forEach(product => {
                const p = document.createElement('p');
                p.textContent = `Product ID: ${product.product_id}, Name: ${product.name}, Verified: ${product.is_verified ? 'Yes' : 'No'}`;
                resultDiv.appendChild(p);
            });
        })
        .catch(error => console.error('Error:', error));
};
