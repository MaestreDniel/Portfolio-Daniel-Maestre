<template>
  <div class="container-fluid text-center text-light bg-main-grad">
    <div class="row d-flex align-items-center justify-content-around m-3">
      <h1 class="col-10 col-md-5">
        ¡Hola! Soy Daniel Maestre. Me alegro de que estés aquí.
      </h1>
      <p class="col-10 col-md-5">
        Me apasiona desarrollar aplicaciones web. Estoy abierto a nuevas oportunidades para seguir
        aprendiendo. Soy una persona disciplinada, creativa, y que presta atención a los pequeños
        detalles.
      </p>
    </div>
    <!-- <img src="@/assets/waves/wave.svg" class="bg-wave" /> -->
    <h2>He desarrollado estos proyectos:</h2>
    <section class="container">
      <div class="row row-cols-1 row-cols-md-3 g-4">
        <article v-for="project in projects" :key="project.id" class="col">
          <ProjectComp :project="project" />
        </article>
      </div>
    </section>
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
  </div>
</template>

<script>
import ProjectComp from "@/components/ProjectComp";
import { getAPI } from "../axios-api";

export default {
  name: "IndexView",
  components: {
    ProjectComp,
  },
  data() {
    return {
      projects: [],
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
