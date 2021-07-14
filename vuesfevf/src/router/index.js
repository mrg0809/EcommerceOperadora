import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Articulo from '../views/Articulo.vue'
import Busqueda from '../views/Busqueda.vue'
import Carrito from '../views/Carrito.vue'
import SubFamilia from '../views/SubFamilia.vue'


const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/:subfamilia_slug/:articulo_slug',
    name: 'Articulo',
    component: Articulo
  },
  {
    path: '/busqueda',
    name: 'Busqueda',
    component: Busqueda
  },
  {
    path: '/carrito',
    name: 'Carrito',
    component: Carrito
  },
  {
    path: '/:subfamilia_slug',
    name: 'SubFamilia',
    component: SubFamilia
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
