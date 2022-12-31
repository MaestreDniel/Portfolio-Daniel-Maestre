<template>
  <h1>Ups, no he podido encontrar esta página</h1>
  <h1>404</h1>
  <RouterLink :to="{ name: 'index' }">Index</RouterLink>
</template>

<script>
export default {
  name: "ErrorView"
}
</script>