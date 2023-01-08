<template>
  <div class="container-fluid text-start text-light text-center bg-main-grad">
    <div class="row d-flex viewport-h-100 align-content-center justify-content-around mx-2 mx-sm-5 transition-1">
      <h1 class="col-12 col-sm-9 my-3 fw-bolder title-xl">
        {{ $t('index.callToAction.first') }} <br>
        <TypewriterItem /> <br>
        {{ $t('index.callToAction.second') }}
      </h1>
      <p class="col-12 col-sm-9 my-3 opacity-80">
        {{ $t("index.summary") }}
      </p>
      <div class="my-4">
        <a href="#projects" class="btn btn-lg btn-primary mx-2">{{ $t("index.more") }}</a>
        <a href="#" class="btn btn-lg btn-custom mx-2">{{ $t("index.contact") }}</a>
      </div>
    </div>
  </div>
  <div class="container-fluid text-center text-light">
    <section id="projects" class="container my-5">
      <h2>{{ $t("index.projects") }}</h2>
      <div class="row row-cols-1 row-cols-md-2 row-cols-xxl-3 g-4">
        <article v-for="project in projects" :key="project.id" class="col">
          <ProjectItem :project="project" />
        </article>
      </div>
    </section>
    <!-- <div class="d-flex viewport-h-100 justify-content-center align-items-center">
      <div v-for="skill in skills" :key="skill.title">
        <SkillItem v-show="skill.current" :skill="skill" class="align-self-start" />
      </div>
    </div> -->
  </div>
</template>

<script>
import ProjectItem from "@/components/ProjectItem";
import TypewriterItem from "@/components/TypewriterItem";
// import SkillItem from "@/components/SkillItem";
import { getAPI } from "../axios-api";

export default {
  name: "IndexView",
  components: {
    ProjectItem,
    TypewriterItem,
    // SkillItem
  },
  data() {
    return {
      projects: []
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
  }
};
</script>
