<template>
  <div id="wrapper">
    <nav class="navbar is-dark">
      
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item"><figure><img src="../src/assets/logoevf.png"></figure></router-link>
        <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu" @click="showMobileMenu = !showMobileMenu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>
      
      <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active': showMobileMenu }">
        <div class="navbar-end">
          <router-link to="/dama" class="navbar-item">Dama</router-link>
          <router-link to="/caballero" class="navbar-item">Caballero</router-link>
          <router-link to="/ninios" class="navbar-item">Youth</router-link>
          <router-link to="/marcas" class="navbar-item">Marcas</router-link>
          <router-link to="/ubicaciones" class="navbar-item">Ubicaciones</router-link>
          
          <div class="navbar-item">
            <div class="buttons">
              <router-link to="/log-in" class="button is-light">Log in</router-link>
              <router-link to="/cart" class="button is-success">
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

    <footer class="footer">
      <p class="has-text-centered">EVF 2021</p>
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
