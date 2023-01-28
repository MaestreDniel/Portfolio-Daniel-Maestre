<template>
  <div class="container text-light m-2">
    <h1>{{ project.title }}</h1>
    <img :src="pathimages + project.thumbnail" class="col-12 fit-contain rounded-3" alt="...">
    <p class="card-text opacity-80">
      {{ project.content }}
    </p>
    <div>
      <p>
        {{ $t('project.date') }}
      </p>
      <p>
        {{ $t('project.published') }}
        {{ project.published }}
      </p>
    </div>
    <a
      :href="project.url"
      target="_blank"
      rel="noreferrer noopener"
      class="btn btn-primary"
    >
      {{ $t("projectItem.view") }} 
      <i class="fa-solid fa-arrow-up-right-from-square" />
    </a>
    <hr>
    <RouterLink :to="{ name: 'index' }">
      Index
    </RouterLink>
  </div>
</template>

<script>
import { getAPI } from "../axios-api";

export default {
  name: "ProjectDetail",
  data() {
    return {
      project: {
        type: Object
      },
    }
  },
  computed: {
    slug() {
      return this.$route.params.slug;
    },
    pathimages() {
      if (process.env.NODE_ENV === 'development') {
        return process.env.VUE_APP_API_MAIN_URL_DEV;
      }
      return "https://danielmaestre.es";
    }
  },
  created() {
    getAPI
      .get(`/projects/${this.slug}/`)
      .then((response) => {
        this.project = response.data;
      })
      .catch((err) => {
        console.log(err);
      });
  },
}
</script>