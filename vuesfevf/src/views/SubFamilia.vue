<template>
    <div class="page-subfamilia">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h2 class="is-size-2 has-text-centered">{{ subfamilia.nombre }}</h2>
            </div>

            <CajaArticulos
        v-for="articulo in subfamilia.subfamilia"
        v-bind:key="articulo.id"
        v-bind:articulo="articulo" />
            
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'
import CajaArticulos from '@/components/CajaArticulos'

export default {
    nombre: 'SubFamilia',
    data() {
        return {
           subfamilia: {
               articulos: []
           } 
        }
    },
    components: {
        CajaArticulos
    },
    mounted() {
        this.getSubFamilia()
    },
    watch: {
        $route(to, from) {
            if(to.name === 'SubFamilia') {
                this.getSubFamilia()
            }
        }
    },
    methods: {
        getSubFamilia(){
            const subfamiliaSlug = this.$route.params.subfamilia_slug
            axios
                .get(`/api/v1/articulos/${subfamiliaSlug}/`)
                .then(response => {
                    this.subfamilia = response.data
                    document.title = this.subfamilia.nombre + ' | EVFstore'
                    console.log(this.subfamilia)
                })
                .catch(error => {
                    console.log(error)

                    toast({
                        message: 'Algo salio mal. Intente de nuevo.',
                        type: 'is-warning',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: 'top-center'
                    })
                })
        }
    }
}
</script>
