<template>
  <div class="home">
    <Vcarousel>
    
    </Vcarousel>

    <div class="columns is-multiline is-centered">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">DESCUBRE LO NUEVO.</h2>
      </div>
      <CajaArticulos
        v-for="articulo in nuevosProductos"
        v-bind:key="articulo.id"
        v-bind:articulo="articulo" />
    </div>
    <hr>
    <div class="columns is-centered is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">NUESTRAS MARCAS.</h2>
      </div>
      <div class="column-is-3">
        <div class="box mx-2">
            <figure class="image is-128x128 mb-4">
              <router-link to="/adidas"><img src="../../src/assets/Adidas.png"></router-link>
            </figure>
        </div>        
      </div>
      <div class="column-is-3">
        <div class="box mx-2">
            <figure class="image is-128x128 mb-4">
              <router-link to="/dc"><img src="../../src/assets/DC.png"></router-link>
            </figure>
        </div>        
      </div>
      <div class="column-is-3">
        <div class="box mx-2">
            <figure class="image is-128x128 mb-4">
              <router-link to="/jansport"><img src="../../src/assets/Jansport.png"></router-link>
            </figure>
        </div>        
      </div>
      <div class="column-is-3">
        <div class="box mx-2">
            <figure class="image is-128x128 mb-4">
              <router-link to="/nike"><img src="../../src/assets/Nike.png"></router-link>
            </figure>
        </div>        
      </div>
      <div class="column-is-3">
        <div class="box mx-2">
            <figure class="image is-128x128 mb-4">
              <router-link to="/puma"><img src="../../src/assets/Puma.png"></router-link>
            </figure>
        </div>        
      </div>
      <div class="column-is-3">
        <div class="box mx-2">
            <figure class="image is-128x128 mb-4">
              <router-link to="/reebok"><img src="../../src/assets/Reebok.png"></router-link>
            </figure>
        </div>        
      </div>
      <div class="column-is-3">
        <div class="box mx-2">
            <figure class="image is-128x128 mb-4">
              <router-link to="/vans"><img src="../../src/assets/Vans.png"></router-link>
            </figure>
        </div>        
      </div>
      <div class="column-is-3">
        <div class="box mx-2">
            <figure class="image is-128x128 mb-4">
              <router-link to="/volcom"><img src="../../src/assets/Volcom.png"></router-link>
            </figure>
        </div>        
      </div>
    </div>
    <hr>
    <div class="columns is-centered is-vcentered is-multiline">
      <div class="column-is-5">
          <figure class="image m-5">
            <img src="../../src/assets/Logo_Square.png">
          </figure>       
      </div>
      <div class="column-is-5 m-5 has-text-justified">
          <h2 class="subtitle"><strong>Quienes somos?</strong></h2>
          <h3>Somos tiendas de ropa, calzado y accesorios de moda.</h3> 
          <h4>Nacimos en Guadalajara, México, en el 2009, impactando primero con bicicletas</h4>
          <h4>y patinetas convirtiéndonos después en el 2012 a EVF STORE con nuestra primera</h4>
          <h4>tienda en León, Guanajuato, creando después una cadena de tiendas en todo México</h4>
          <h4>que se esfuerza por incluir y entregar todos los aspectos de nuestro estilo de</h4>
          <h4>vida a los consumidores.</h4>
          <br/>
          <h3>Somos EVF y somos tu estilo de vida.</h3>      
      </div>    
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
