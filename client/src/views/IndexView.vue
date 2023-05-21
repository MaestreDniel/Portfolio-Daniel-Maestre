<template>
  <div class="container-fluid text-start text-light text-center bg-main-grad">
    <div class="row d-flex viewport-h-100 align-content-center justify-content-around mx-2 mx-sm-5 transition-1">
      <h1 class="col-12 col-sm-9 my-3 title title-xxl">
        {{ $t('index.callToAction.first') }} <br>
        <TypewriterItem /> <br>
        {{ $t('index.callToAction.second') }}
      </h1>
      <p class="col-12 col-sm-10 col-md-8 my-3 opacity-80">
        {{ $t("index.summary") }}
      </p>
      <div class="my-4">
        <a href="#works" class="btn btn-lg btn-primary mx-2">{{ $t("index.more") }}</a>
        <!-- <a href="#" class="btn btn-lg btn-custom mx-2">{{ $t("index.contact") }}</a> -->
      </div>
    </div>
  </div>
  <div class="container text-light px-4">
    <section id="works" class="container py-3">
      <h2 class="title title-xl mb-5 pb-4">
        {{ $t("index.works") }}
      </h2>
      <svg height="500" width="10" class="d-none d-lg-block position-absolute start-50 translate-middle-x">
        <line
          x1="5"
          y1="10"
          x2="5"
          y2="440"
          stroke="#edfcfe"
          stroke-width="4"
        />
      </svg>
      <article v-for="(work, index) in works" :key="work.id" class="my-5">
        <WorkItem :work="work" :index="index" />
      </article>
    </section>
    <section id="projects" class="container">
      <h2 class="title title-xl mb-5 pb-4">
        {{ $t("index.projects") }}
      </h2>
      <div class="row g-5">
        <article v-for="(project, index) in projects" :key="project.id" class="my-5">
          <ProjectItem :project="project" :index="index" />
        </article>
      </div>
    </section>
  </div>
</template>

<script>
import ProjectItem from "@/components/ProjectItem";
import TypewriterItem from "@/components/TypewriterItem";
import WorkItem from "@/components/WorkItem"
import { getAPI } from "../axios-api";

export default {
  name: "IndexView",
  components: {
    ProjectItem,
    TypewriterItem,
    WorkItem
  },
  data() {
    return {
      projects: [],
      works: []
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
    
    getAPI
      .get("/works/")
      .then((response) => {
        this.works = response.data;
      })
      .catch((err) => {
        console.log(err);
      });
  }
};
</script>
