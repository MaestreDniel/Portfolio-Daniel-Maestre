<template>
  <!-- Proyecto -->
  <div class="card h-100 bg-dark">
    <img :src="pathimages + project.thumbnail" class="card-img-top" alt="..." />
    <div class="card-body">
      <h5 class="card-title">{{ project.title }}</h5>
      <p class="card-text">{{ project.content }}</p>
      <a :href="project.url" target="_blank" rel="noreferrer noopener" class="btn btn-primary mx-2">Ver proyecto <i class="fa-solid fa-arrow-up-right-from-square"></i></a>
      <a href="#" class="btn btn-custom mx-2">Más detalles</a>
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
      // pathimages: "https://danielmaestre.es",
      pathimages: "http://127.0.0.1:8000",
    };
  },
};
</script>
