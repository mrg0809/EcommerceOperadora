import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Articulo from '../views/Articulo.vue'
import Busqueda from '../views/Busqueda.vue'
import Carrito from '../views/Carrito.vue'
import Checkout from '../views/Checkout.vue'
import Contacto from '../views/Contacto.vue'
import Devolucion from '../views/Devolucion.vue'
import Marca from '../views/Marca.vue'
import Privacidad from '../views/Privacidad.vue'
import SubFamilia from '../views/SubFamilia.vue'
import Success from '../views/Success.vue'
import Terminos from '../views/Terminos.vue'



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
    path: '/carrito/checkout',
    name: 'Checkout',
    component: Checkout
  },
  {
    path: '/carrito/success',
    name: 'Success',
    component: Success
  },
  {
    path: '/contacto',
    name: 'Contacto',
    component: Contacto
  },
  {
    path: '/devolucion',
    name: 'Devolucion',
    component: Devolucion
  },
  {
    path: '/:marca_slug',
    name: 'Marca',
    component: Marca
  },
  {
    path: '/privacidad',
    name: 'Privacidad',
    component: Privacidad
  },
  {
    path: '/:subfamilia_slug',
    name: 'SubFamilia',
    component: SubFamilia
  },
  {
    path: '/terminos',
    name: 'Terminos',
    component: Terminos
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
