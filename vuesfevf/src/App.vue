<template>
  <div id="wrapper">
    <nav class="navbar is-black has-shadow is-fixed-top">
      
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item"><figure><img src="../src/assets/logoevf.png"></figure></router-link>
        <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu" @click="showMobileMenu = !showMobileMenu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>
      
      <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active': showMobileMenu }">
        <div class="navbar-start">
          <router-link to="/subfamilia/dama" class="navbar-item">Dama</router-link>
          <router-link to="/subfamilia/caballero" class="navbar-item">Caballero</router-link>
          <router-link to="/subfamilia/ninios" class="navbar-item">Niños</router-link>
          <div class="navbar-item has-dropdown is-hoverable">
            <a class="navbar-link">Marcas</a>
            <div class="navbar-dropdown">
              <router-link to="/adidas" class="navbar-item">Adidas</router-link>
              <router-link to="/dc" class="navbar-item">DC</router-link>
              <router-link to="/jansport" class="navbar-item">Jansport</router-link>
              <router-link to="/nike" class="navbar-item">Nike</router-link>
              <router-link to="/puma" class="navbar-item">Puma</router-link>
              <router-link to="/reebok" class="navbar-item">Reebok</router-link>
              <router-link to="/vans" class="navbar-item">Vans</router-link>
              <router-link to="/volcom" class="navbar-item">Volcom</router-link>
            </div>
            
          </div>
          <router-link to="/ubicacion" class="navbar-item">Ubicaciones</router-link>
        </div>
        <div class="navbar-end">
          <div class="navbar-item">
            <form method="get" action="/busqueda">
              <div class="field has-addons">
                <div class="control">
                  <input type="text" class="input" placeholder="Buscar Articulo" name="busqueda">
                </div>
                <div class="control">
                  <button class="button is-dark">
                    <span class="icon">
                      <i class="fas fa-search"></i>
                    </span>
                  </button>
                </div>
              </div>
            </form>
          </div>
          <div class="navbar-item">
            <div class="buttons">
              <router-link to="/carrito" class="button is-dark">
                <span class="icon"><i class="fas fa-shopping-cart"></i></span>
                <span>Carrito ({{ cartTotalLength }})</span>
              </router-link>
            </div>
          </div>  
        </div>
      </div>
    </nav>

    <section class="section">
      <router-view/>
    </section>

    <footer class="footer has-background-black">
      <div class="columns is-centered is-multiline">
        <div class="column is-auto is-centered ml-6">
          <img src="https://img.icons8.com/color/48/000000/amex.png"/>
          <img src="https://img.icons8.com/color/48/000000/visa.png"/>
          <img src="https://img.icons8.com/color/48/000000/mastercard.png"/>
        </div>
        <div class="column is-one-quarter">
          <div>
            <a href="https://www.facebook.com/evfstoremx/" target="_blank"><img src="https://img.icons8.com/nolan/64/facebook.png"/></a>
            <a href="https://www.instagram.com/evfstore/" target="_blank"><img src="https://img.icons8.com/nolan/64/instagram-new.png"/></a>
          </div>
          <a href="https://icons8.com/icon/43625/instagram" class="has-text-black">Icons by Icons8</a>
        </div>
      </div>
        <div class="columns is-multiline is-centered">
          <router-link to="/contacto" class="has-text-grey">Contacto - </router-link>
          <router-link to="/terminos" class="has-text-grey">Terminos y condiciones</router-link>
          <p class="has-text-centered has-text-white">--EVF 2021--</p>
          <router-link to="/privacidad" class="has-text-grey">Privacidad - </router-link>
          <router-link to="/devolucion" class="has-text-grey"> Politica de devoluciones</router-link>
        </div>
      
    </footer>
  </div>

</template>

<script>
export default {
  data() {
    return {
      showMobileMenu: false,
      cart: {
        items: []
      }
    }
  },
  beforeCreate() {
    this.$store.commit('initializeStore')
  },
  mounted() {
    this.cart = this.$store.state.cart
  },
  computed: {
    cartTotalLength() {
      let totalLength = 0

      for (let i = 0; i < this.cart.items.length; i++) {
        totalLength += this.cart.items[i].cantidad
      }
      return totalLength
    }
  }
}
</script>

<style lang="scss">
@import '../../node_modules/bulma';
</style>
