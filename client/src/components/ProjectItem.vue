<template>
  <div
    :class="{
      'd-md-flex': index % 2 === 0,
      'd-md-flex flex-row-reverse': index % 2 !== 0
    }"
  >
    <img :src="pathimages + project.thumbnail" class="col-12 col-md-6 fit-contain rounded" alt="...">
    <div class="col-12 col-md-6 p-4">
      <h2 class="mb-3">
        {{ project.title }}
      </h2>
      <p class="card-text opacity-80">
        {{ project.content }}
      </p>
      <a
        :href="project.url"
        target="_blank"
        rel="noreferrer noopener"
        class="btn btn-primary"
      >
        {{ $t("projectItem.view") }} 
        <i class="fa-solid fa-arrow-up-right-from-square" />
      </a>
      <RouterLink 
        :to="{ name: 'project.show', params: { slug: project.slug } }"
        class="btn btn-custom mx-3"
      >
        {{ $t("projectItem.detail") }}
      </RouterLink>
    </div>
  </div>
</template>

<script>
export default {
  name: "ProjectItem",
  props: {
    project: {
      type: Object,
      required: true
    },
    index: {
      type: Number,
      required: true
    }
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
