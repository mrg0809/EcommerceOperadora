<template>
  <div class="home">
    <section class="hero has-carousel">
      <div class="hero-carousel">
        <div class="item-1">
            <img src="../assets/bannerevf1.png">
          </div>
          <div class="item-2">
            <img src="../assets/bannerevf2.png">
          </div>
      </div>
    </section>

    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">Nuevos Productos</h2>
      </div>
      <CajaArticulos
        v-for="articulo in nuevosProductos"
        v-bind:key="articulo.id"
        v-bind:articulo="articulo" />
      </div>
    </div>
  
</template>

<script>
import axios from 'axios'
import carousel from 'bulma-carousel/dist/js/bulma-carousel.min.js'
import CajaArticulos from '@/components/CajaArticulos'

export default {
  name: 'Home',
  data() {
    return {
      nuevosProductos: []
    }
  },
  components: {
    CajaArticulos
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
