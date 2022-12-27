<template>
  <div class="card h-100 bg-dark">
    <img :src="pathimages + project.thumbnail" class="card-img-top" alt="..." />
    <div class="card-body">
      <h5 class="card-title">{{ project.title }}</h5>
      <p class="card-text">{{ project.content }}</p>
      <a :href="project.url" target="_blank" rel="noreferrer noopener" class="btn btn-primary mx-2">
        {{ $t("projectItem.view") }} 
        <i class="fa-solid fa-arrow-up-right-from-square"></i>
      </a>
      <a href="#" class="btn btn-custom mx-2">{{ $t("projectItem.detail") }} </a>
    </div>
  </div>
</template>

<script>
export default {
  name: "ProjectItem",
  props: {
    project: Object
  },
  data() {
    if (process.env.NODE_ENV === 'development') {
      return {
        pathimages: process.env.VUE_APP_API_MAIN_URL_DEV
      };
    } else {
      return {
        pathimages: "https://danielmaestre.es"
      };
    }
  },
};
</script>
