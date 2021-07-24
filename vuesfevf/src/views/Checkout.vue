<template>
    <div class="page-checkout">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Pantalla de Pago</h1>
            </div>
            <div class="column is-12 box">
                <table class="table is-fullwidth">
                    <thead>
                        <tr>
                            <th>Articulo</th>
                            <th>Talla</th>
                            <th>Precio</th>
                            <th>Cantidad</th>
                            <th>Total</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr
                            v-for="item in cart.items"
                            v-bind:key="item.articulo.id"
                        >
                            <td>{{ item.articulo.modelo }}</td>
                            <td> Talla </td>
                            <td>{{ item.articulo.precio }}</td>
                            <td>{{ item.cantidad }}</td>
                            <td>{{ getItemTotal(item).toFixed(2) }}</td>
                        </tr>
                    </tbody>
                    <tfoot>
                        <tr>
                            <td colspan="3">Total</td>
                            <td>{{ cartTotalLength }}</td>
                            <td>${{ cartTotalPrice.toFixed(2) }}</td>
                        </tr>
                    </tfoot>
                </table>
            </div>
            <div class="column is-12 box">
                <h2 class="subtitle">Detalles de envio</h2>
                <p class="has-text-grey mb-4">*Campo requerido.</p>
                <div class="columns is-multiline">
                    <div class="column is-6">
                        <div class="field">
                            <label>Nombre*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="first_name">
                            </div>
                        </div>

                        <div class="field">
                            <label>Apellido*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="last_name">
                            </div>
                        </div>

                        <div class="field">
                            <label>Email*</label>
                            <div class="control">
                                <input type="email" class="input" v-model="email">
                            </div>
                        </div>

                        <div class="field">
                            <label>Telefono*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="phone">
                            </div>
                        </div>
                    </div>
                    <div class="column is-6">
                        <div class="field">
                            <label>Direccion*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="adress">
                            </div>
                        </div>

                        <div class="field">
                            <label>Colonia*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="adress2">
                            </div>
                        </div>

                        <div class="field">
                            <label>C.P.*</label>
                            <div class="control">
                                <input type="email" class="input" v-model="zipcode">
                            </div>
                        </div>

                        <div class="field">
                            <label>Ciudad*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="city">
                            </div>
                        </div>
                    </div>
                </div>

                 <div class="notification is-warning mt-4" v-if="errors.length">
                    <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                </div>
                <hr>

                <div id="card-element" class="mb-5"></div>

                <template v-if="cartTotalLength">
                    <hr>
                    <button class="button is-black" @click="submitForm">Pagar con Stripe</button>
                </template>
                    
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
name: 'Checkout',
    data() {
        return {
            cart: {
                items: []
            },
            stripe: {},
            card: {},
            first_name: '',
            last_name: '',
            email: '',
            phone: '',
            adress: '',
            adress2:'',
            zipcode: '',
            city: '',
            errors: []
        }
    },
    mounted() {
        document.title = 'Checkout | EVFstore'

        this.cart = this.$store.state.cart

        if (this.cartTotalLength > 0) {
            this.stripe = Stripe('pk_test_51JDgmbDKHFM41Os3nR07xS2V2KkP7ghU7HqLY5Ko8MsyydHQQwo5DTksz0XpZcNzxnepFtdfz6y4a8GowFfLaetn00hVDnAgSo')
            const elements = this.stripe.elements();
            this.card = elements.create('card', { hidePostalCode: true })

            this.card.mount('#card-element')
        }
    },
    methods: {
        getItemTotal(item) {
            return item.cantidad * item.articulo.precio
        },
        submitForm() {
            this.errors = []

            if (this.first_name === '') {
                this.errors.push('Campo de nombre esta vacio.')
            }

            if (this.last_name === '') {
                this.errors.push('Campo de apellido esta vacio.')
            }

            if (this.email === '') {
                this.errors.push('Campo de email esta vacio.')
            }

            if (this.phone === '') {
                this.errors.push('Campo de telefono esta vacio.')
            }

            if (this.adress === '') {
                this.errors.push('Campo de direccion esta vacio.')
            }

            if (this.adress2 === '') {
                this.errors.push('Campo de colonia esta vacio.')
            }

            if (this.zipcode === '') {
                this.errors.push('Campo de codigo postal esta vacio.')
            }

            if (this.city === '') {
                this.errors.push('Campo de ciudad esta vacio.')
            }

            if (!this.errors.length) {
                this.stripe.createToken(this.card).then(result => {
                    if (result.error) {
                        this.errors.push('Algo salio mal con Stripe. Intenta de nuevo.')
                        console.log(result.error.message)
                    }else {
                        this.stripeTokenHandler(result.token)
                    }
                })
            }

        },
        async stripeTokenHandler(token) {
            const items = []

            for (let i=0; i<this.cart.items.length; i++) {
                const item = this.cart.items[i]
                const obj = {
                    articulo: item.articulo.id,
                    cantidad: item.cantidad,
                    precio: item.articulo.precio * item.cantidad
                }

                items.push(obj)
            }

            const data = {
                'first_name': this.first_name,
                'last_name': this.last_name,
                'email': this.email,
                'adress': this.adress,
                'adress2': this.adress2,
                'zipcode': this.zipcode,
                'city': this.city,
                'phone': this.phone,
                'stripe_token': token.id,
                'articulos': items,
                
            }
            await axios
                .post('/api/v1/checkout/', data)
                .then(response => {
                    this.$store.commit('clearCart')
                    this.$router.push('/carrito/success')
                })
                .catch(error => {
                    this.errors.push('Algo salio mal. Intente de nuevo')

                    console.log(error)
                })
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
