<template>
  <div class="container-fluid text-start text-light bg-main">
    <div class="row d-flex viewport-h-100 align-content-center justify-content-around mx-2 mx-sm-5">
      <h1 class="col-12 transition-1 my-3">Tus ideas: desde tu mente hasta la web.</h1>
      <p class="col-12 transition-1 my-3">
        Soy Daniel Maestre. Me dedico al <b>desarrollo web</b> y soy de Palma de Mallorca. Tengo
        habilidad tanto para front-end como para back-end. Soy alguien versátil para las tecnologías
        y me mantengo siempre al día para afrontar los retos de esta profesión.
      </p>
      <div class="my-4">
        <a href="#" class="btn btn-lg btn-primary transition-1-delay-1 me-2">Saber más</a>
        <a href="#" class="btn btn-lg btn-custom transition-1-delay-1 mx-2">Quiero contactar</a>
      </div>
    </div>
  </div>
  <div class="container-fluid text-center text-light bg-main-grad">
    <section class="container my-5">
      <h2>He desarrollado estos proyectos:</h2>
      <div class="row row-cols-1 row-cols-md-2 row-cols-xxl-3 g-4">
        <article v-for="project in projects" :key="project.id" class="col">
          <ProjectComp :project="project" />
        </article>
      </div>
    </section>
    <div class="d-flex viewport-h-100 justify-content-center align-items-center">
      <div v-for="skill in skills" :key="skill.title">
        <SkillComp v-show="skill.current" :skill="skill" class="align-self-start" />
      </div>
    </div>
  </div>
</template>

<script>
import ProjectComp from "@/components/ProjectComp";
import SkillComp from "@/components/SkillComp";
import { getAPI } from "../axios-api";

export default {
  name: "IndexView",
  components: {
    ProjectComp,
    SkillComp,
  },
  data() {
    return {
      projects: [],
      skills: [
        { title: "fa-solid fa-code", current: true, description: "Desarrollo Web" },
        { title: "fa-solid fa-check", current: false, description: "Encontrar soluciones" },
        { title: "fa-solid fa-gears", current: false, description: "Perseverancia" },
        { title: "fa-solid fa-lightbulb", current: false, description: "Creatividad" },
        { title: "fa-solid fa-cubes", current: false, description: "Aplicaciones organizadas" },
      ],
      i: 0,
    };
  },
  methods: {
    animate() {
      let skill = this.skills;
      if (this.i < skill.length - 1) {
        skill[this.i + 1].current = true;
        skill[this.i].current = false;
        this.i++;
      } else {
        this.i = 0;
        skill[this.i].current = true;
        skill[skill.length - 1].current = false;
      }
    },
  },
  mounted: function () {
    this.timer = setInterval(() => {
      this.animate();
    }, 5000);
  },
  created() {
    getAPI
      .get("/proyectos/")
      .then((response) => {
        this.projects = response.data;
      })
      .catch((err) => {
        console.log(err);
      });
  },
};
</script>
