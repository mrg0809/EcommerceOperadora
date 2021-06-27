<template>
  <div class="home">
    <section class="hero is-medium is-dark mb-6">
      <div class="hero-body has-text-centered">
        <p class="title mb-6">
          EVF Store
        </p>
        <p class="subtitle">
          Evolution, Vitality, Freedom.
        </p>
      </div>
    </section>

    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">Nuevos Productos</h2>
      </div>
      <div class="column-is-3" v-for="articulo in nuevosProductos" v-bind:key="articulo.id">
        <div class="box">
          <figure class="image mb-4">
            <img v-bind:src="articulo.get_miniatura">
          </figure>

          <h3 class="is-size-4">{{ articulo.modelo }}</h3>
          <p class="is-size-6 has-text-grey">${{ articulo.precio }}</p>

          <router-link v-bind:to="articulo.get_absolute_url" class="button is-dark mt-4">Detalles</router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Home',
  data() {
    return {
      nuevosProductos: []
    }
  },
  components: {
  },
  mounted() {
    this.getNuevosProductos()
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
