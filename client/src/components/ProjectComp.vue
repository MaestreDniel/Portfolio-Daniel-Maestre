<template>
  <!-- Proyecto -->
  <div class="card h-100 bg-dark">
    <img :src="pathimages + project.thumbnail" class="card-img-top" alt="..." />
    <div class="card-body">
      <h5 class="card-title">{{ project.title }}</h5>
      <p class="card-text">{{ project.content }}</p>
      <a href="#" class="btn btn-primary mx-2">Ver proyecto</a>
      <a href="#" class="btn btn-outline-primary mx-2">Más detalles</a>
    </div>
  </div>
  <!-- Fin Proyecto -->
</template>

<script>
export default {
  name: "ProjectComp",
  props: ["project"],
  data() {
    return {
      pathimages: "https://danielmaestre.es",
    };
  },
};
</script>
