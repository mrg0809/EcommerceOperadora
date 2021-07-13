<template>
    <div class="page-search">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Busqueda</h1>
                <h2 class="is-size-5 has-text-black">Resultados para: "{{ busqueda }}"</h2>
            </div>
            <CajaArticulos
                v-for="articulo in articulos"
                v-bind:key="articulo.id"
                v-bind:articulo="articulo" />
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import CajaArticulos from '@/components/CajaArticulos.vue'

export default {
    name: 'Busqueda',
    components: {
        CajaArticulos
    },
    data() {
        return {
            articulos: [],
            busqueda: ''
        }
    },
    mounted() {
        document.title = 'Busqueda | EVFstore'
        let uri = window.location.search.substring(1)
        let params = new URLSearchParams(uri)

        if (params.get('busqueda')) {
            this.busqueda = params.get('busqueda')
            this.performSearch()
        }
    },
    methods: {
        performSearch() {
            axios
                .post('/api/v1/articulos/busqueda/', {'busqueda': this.busqueda})
                .then(response => {
                    this.articulos = response.data
                })
                .catch(error => {
                    console.log(error)
                })
        }
    }
}
</script>
