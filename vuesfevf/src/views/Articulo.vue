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
                        <option> {{ articulo.talla }}</option>
                    </select>
                </div>
                <br>
                <p>Cantidad:</p>
                <div class="field is-dark has-addons">
                    <div class="control">
                        <input type="number" class="input" min="1" v-model="cantidad">
                    </div>
                    <div class="control">
                        <a class="button is-dark">Agregar al carrito</a>
                    </div>
                </div>
            </div>
        </div>
    </div>    
</template>

<script>
import axios from 'axios'

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
                })
                .catch( error=> {
                    console.log(error)
                })
        }
    }
}
</script>
