<template>
  <div class="text-center">
    <h2 class="">
      Estamos en portfolio, prueba
    </h2>
    <button type="button" class="btn btn-primary">Primary</button>
    <div v-for="project in projects" :key="project.id" class="">
      <!-- <router-link
        :to="{
          name: 'ProjectView',
          params: {
            id: project.id,
            title: project.title,
            thumbnail: project.thumbnail,
            slug: project.slug,
            content: project.content,
          },
        }"
      >
        <p>{{ project.title }}</p>
      </router-link> -->

      <div>{{ project.id }}</div>
      <div>{{ project.title }}</div>
      <img :src="pathimages + project.thumbnail" />
      <div>{{ project.content }}</div>
    </div>
  </div>
</template>

<script>
import { getAPI } from "../axios-api";

export default {
  name: "IndexView",
  data() {
    return {
      projects: [],
      pathimages: 'https://danielmaestre.es'
    };
  },
  created() {
    getAPI
      .get("/proyectos/")
      .then((response) => {
        this.projects = response.data;
        // console.log(this.projects);
      })
      .catch((err) => {
        console.log(err);
      });
  },
};
</script>
