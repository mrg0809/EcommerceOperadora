<template>
    <div class="column-is-3">
        <div class="box mx-2">
            <figure class="image mb-4">
            <img v-bind:src="articulo.get_miniatura">
            </figure>

            <h3 class="is-size-4">{{ articulo.modelo }}</h3>
            <p class="is-size-6 has-text-grey">${{ articulo.precio }}</p>

            <router-link v-bind:to="articulo.get_absolute_url" class="button is-dark mt-4">Detalles</router-link>
        </div>
    </div>
</template>

<script>
export default {
    name: 'CajaArticulos',
    props: {
        articulo: Object
    }
}
</script>
