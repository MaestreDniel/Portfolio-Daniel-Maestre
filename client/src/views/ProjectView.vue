<template>
  <div class="">
    <h1>
      Ha funcionado
      <span class="">{{ $route.params.title }}</span>
    </h1>
    <article v-for="project in projects" :key="project.id" class="col">
      <ProjectItem :project="project" />
    </article>
    <div class="">{{ $route.params.content }}</div>
  </div>
</template>

<script>
import { getAPI } from "../axios-api";
import ProjectItem from "@/components/ProjectItem";

export default {
  name: "ProjectDetail",
  components: {
    ProjectItem,
  },
  /* props: {
    projects: []
  }, */
  data() {
    return {
      projects: [],
    };
  },
  created() {
    getAPI
      .get("/projects/")
      .then((response) => {
        this.projects = response.data;
      })
      .catch((err) => {
        console.log(err);
      });
  },
}
</script>