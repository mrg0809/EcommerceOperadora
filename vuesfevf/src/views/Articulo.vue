<template>
    <div class="page-product">
        <div class="column is-multiline">
            <div class="column is-9">
                <figure class="image mb-6">
                    <img v-bind:src="articulo.get_image">
                </figure>
                <h1 class="title">{{ articulo.modelo }}</h1>
                <p>{{ articulo.descripcion }}</p>
            </div>

            <div class="column is-3">
                <h2 class="subtitle"></h2>
                <p><strong>Precio: </strong>${{ articulo.precio }}</p>

                <div class="field has-addons mt-6">
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
