<template>
    <div class="page-carrito">
        <div class="column is-12">
            <h1 class="title">Carrito de compras</h1>
        </div>
        <div class="column is-12 box">
            <table class="table is-fullwidth" v-if="cartTotalLength">
                <thead>
                    <tr>
                        <th>Articulo</th>
                        <th>Talla</th>
                        <th>Precio</th>
                        <th>Cantidad</th>
                        <th>Total</th>
                        <th></th>
                    </tr>
                </thead>
                <tbody>
                    <ArticuloCarrito
                        v-for="item in cart.items"
                        v-bind:key="item.articulo.id"
                        v-bind:initialItem="item"
                        v-on:removeFromCart="removeFromCart" />
                </tbody>
            </table>
            <p v-else>Aun no has agregado productos a tu carrito.</p>
        </div>

        <div class="column is-12 box has-text-centered">
            <h2 class="subtitle">Subtotal</h2>
             <strong>${{ cartTotalPrice.toFixed(2) }}</strong>, {{ cartTotalLength }} articulos
             <hr>
             <router-link to="/carrito/checkout" class="button is-dark">Continuar a pantalla de Pago</router-link>
        </div>

    </div>
</template>

<script>
import axios from 'axios'
import ArticuloCarrito from '@/components/ArticuloCarrito.vue'
export default {
    name: 'Carrito',
    components: {
        ArticuloCarrito
    },
    data() {
        return {
            cart: {
                items: []
            }
        }
    },
    mounted() {
        this.cart = this.$store.state.cart
    },
    methods: {
        removeFromCart(item) {
            this.cart.items = this.cart.items.filter(i => i.articulo.id !== item.articulo.id)
        }
    },
    computed: {
        cartTotalLength() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.cantidad
            }, 0)
        },
        cartTotalPrice() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.cantidad * curVal.articulo.precio
            }, 0)
        }
    }
}
</script>
