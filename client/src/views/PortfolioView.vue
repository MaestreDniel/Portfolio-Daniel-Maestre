<template>
  <div class="relative bg-gray-50 pt-16 pb-20 px-4 sm:px-6 lg:pt-24 lg:pb-28 lg:px-8">
    <div class="relative max-w-7xl mx-auto">
      <div class="text-center">
        <h2 class="text-3xl tracking-tight font-extrabold text-gray-900 sm:text-4xl">
          Estamos en portfolio, prueba
        </h2>
      </div>
      <div class="mt-12 max-w-lg mx-auto grid gap-5 lg:grid-cols-3 lg:max-w-none">
        <div
          v-for="project in projects"
          :key="project.id"
          class="flex flex-col rounded-lg shadow-lg overflow-hidden"
        >
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
    </div>
  </div>
</template>

<script>
import { getAPI } from "../axios-api";

export default {
  name: "PortfolioView",
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
        console.log("Post API has recieved data");
        this.projects = response.data;
        console.log(this.projects);
      })
      .catch((err) => {
        console.log(err);
      });
  },
};
</script>
