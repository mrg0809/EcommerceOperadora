<template>
    <div class="page-product">
        <div class="columns is-multiline">
            <div class="column is-6">
                <figure class="image mb-6">
                    <img v-bind:src="articulo.get_image">
                </figure>
            </div>

            <div class="column is-6">
                <h1 class="title">{{ articulo.modelo }}</h1>
                <h2 class="subtitle">{{ articulo.descripcion }}</h2>
                <p><strong>Precio: </strong>${{ articulo.precio }}</p>
                <hr>
                <p>Talla:</p>
                <div class="select is-dark has-addons">
                    <select>
                        <option> {{ }}</option>
                    </select>
                </div>
                <br>
                <p>Cantidad:</p>
                <div class="field is-dark has-addons">
                    <div class="control">
                        <input type="number" class="input" min="1" v-model="cantidad">
                    </div>
                    <div class="control">
                        <a class="button is-dark" @click="addToCart">Agregar al carrito</a>
                    </div>
                </div>
            </div>
        </div>
    </div>    
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
    name: 'Articulo',
    data(){
        return {
            articulo: {},
            cantidad: 1
        }
    },
    mounted() {
        this.getArticulo()
    },
    methods: {
        getArticulo(){
            const subfamilia_slug = this.$route.params.subfamilia_slug
            const articulo_slug = this.$route.params.articulo_slug

            axios
                .get(`/api/v1/articulos/${subfamilia_slug}/${articulo_slug}`)
                .then(response => {
                    this.articulo = response.data
                    document.title = this.articulo.modelo + ' | EVFstore'
                })
                .catch( error=> {
                    console.log(error)
                })
        },
        addToCart() {
            if (isNaN(this.cantidad) || this.cantidad < 1) {
                this.cantidad = 1
            }

            const item = {
                articulo: this.articulo,
                cantidad: this.cantidad
            }

            this.$store.commit('addToCart', item)

            toast({
                message: 'El producto ha sido agregado al carrito de compras',
                type: 'is-success',
                dismissible: true,
                pauseOnHover: true,
                duration: 3000,
                position: 'top-center',
            })
        }
    }
}
</script>
