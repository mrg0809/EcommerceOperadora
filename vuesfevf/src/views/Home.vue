<template>
  <div class="home">
    <Vcarousel>
    
    </Vcarousel>

    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">DESCUBRE LO NUEVO.</h2>
      </div>
      <CajaArticulos
        v-for="articulo in nuevosProductos"
        v-bind:key="articulo.id"
        v-bind:articulo="articulo" />
    </div>
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">NUESTRAS MARCAS.</h2>
      </div>

      
    </div>

    
  
</template>

<script>
import axios from 'axios'
import Vcarousel from '@/components/Vcarousel'
import CajaArticulos from '@/components/CajaArticulos'

export default {
  name: 'Home',
  data() {
    return {
      nuevosProductos: []
    }
  },
  components: {
    CajaArticulos,
    Vcarousel
  },
  mounted() {
    this.getNuevosProductos()

    document.title = 'Inicio' + ' | EVFstore'
  },
  methods: {
    getNuevosProductos() {
      axios
        .get('api/v1/lastest-products/')
        .then(response => {
          this.nuevosProductos = response.data
        })
        .catch(error => {
          console.log(error)
        })
    }    
  }
}
</script>
