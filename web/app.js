new Vue({
    el: '#admin',
    data: {
        products: [],
        newProduct: { name: '', price: 0 }
    },
    methods: {
        fetchProducts() {
            fetch('/api/products')
                .then(response => response.json())
                .then(data => this.products = data);
        },
        addProduct() {
            fetch('/api/products', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(this.newProduct)
            }).then(this.fetchProducts);
            this.newProduct = { name: '', price: 0 };
        },
        updateProduct(product) {
            fetch(`/api/products/${product.id}`, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(product)
            }).then(this.fetchProducts);
        },
        deleteProduct(id) {
            fetch(`/api/products/${id}`, { method: 'DELETE' })
                .then(this.fetchProducts);
        }
    },
    mounted() {
        this.fetchProducts();
    }
});

new Vue({
    el: '#app',
    data: {
        products: [],
        cart: []
    },
    methods: {
        fetchProducts() {
            fetch('/api/products')
                .then(response => response.json())
                .then(data => this.products = data);
        },
        orderProduct(product) {
            this.cart.push(product);
        }
    },
    mounted() {
        this.fetchProducts();
    }
});
new Vue({
    el: '#app',
    data: {
        products: [],
        cart: []
    },
    computed: {
        totalPrice() {
            return this.cart.reduce((total, item) => total + item.price, 0);
        }
    },
    methods: {
        // Các method khác ...
    },
    mounted() {
        this.fetchProducts();
    }
});



