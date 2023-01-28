<template>
  <div
    :class="{
      'd-lg-flex g-4': index % 2 === 0,
      'd-lg-flex flex-row-reverse g-4': index % 2 !== 0
    }"
  >
    <div class="container-image m-4">
      <RouterLink 
        :to="{ name: 'project.show', params: { slug: project.slug } }"
        class="overlay-image-link"
      >
        <span class="position-absolute top-50 start-50 translate-middle text-light h2">
          {{ $t("projectItem.detail") }}
        </span>
      </RouterLink>
      <img :src="pathimages + project.thumbnail" class="col-12 fit-contain rounded-3" alt="...">
    </div>
    <div class="col-12 col-lg-6 p-4">
      <h2 class="mb-3 title-link">
        <a
          :href="project.url"
          target="_blank"
          rel="noreferrer noopener"
        >
          {{ project.title }}
          <i class="fa-solid fa-arrow-up-right-from-square mx-2" />
        </a>
      </h2>

      <p class="card-text opacity-80">
        {{ project.content }}
      </p>
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
