<template>
    <div class="page-marca">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h2 class="is-size-2 has-text-centered">{{ marca.nombre }}</h2>
            </div>

            <CajaArticulos
        v-for="articulo in marca.marca"
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
    nombre: 'Marca',
    data() {
        return {
           marca: {
               articulos: []
           } 
        }
    },
    components: {
        CajaArticulos
    },
    mounted() {
        this.getMarca()
    },
    watch: {
        $route(to, from) {
            if(to.name === 'Marca') {
                this.getMarca()
            }
        }
    },
    methods: {
        getMarca(){
            const marcaSlug = this.$route.params.marca_slug
            axios
                .get(`/api/v1/marca/${marcaSlug}/`)
                .then(response => {
                    this.marca = response.data
                    document.title = this.marca.nombre + ' | EVFstore'
                    console.log(this.marca)
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
