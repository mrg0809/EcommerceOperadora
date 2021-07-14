<template>
    <tr>
        <td><router-link :to="item.articulo.get_absolute_url">{{ item.articulo.modelo }}</router-link></td>
        <td>talla</td>
        <td>${{ item.articulo.precio }}</td>
        <td> 
            <a @click="decrementQuantity(item)">- </a>
            {{ item.cantidad }}
            <a @click="incrementQuantity(item)"> +</a>
        </td>
        <td>${{ totalArticulos(item).toFixed(2) }}</td>
        <td><button class="delete" @click="removeFromCart(item)"></button></td>
    </tr>
</template>

<script>
export default {
    name: 'ArticuloCarrito',
    props: {
        initialItem: Object
    },
    data() {
        return {
            item: this.initialItem
        }
    },
    methods: {
        totalArticulos(item){
            return item.cantidad * item.articulo.precio
        },
        decrementQuantity(item) {
            item.cantidad -= 1
            if(item.cantidad === 0) {
                this.$emit('removeFromCart', item)
            }
            this.updateCart()
        },
        incrementQuantity(item) {
            item.cantidad += 1
            this.updateCart()
        },
        updateCart() {
            localStorage.setItem('cart', JSON.stringify(this.$store.state.cart))
        },
        removeFromCart(item) {
            this.$emit('removeFromCart', item)

            this.updateCart()
        }
    }
}
</script>