<template>
  <div
    :class="{
      'd-lg-flex g-4': index % 2 === 0,
      'd-lg-flex flex-row-reverse g-4': index % 2 !== 0
    }"
  >
    <div
      :class="{
        'container-image me-lg-5': index % 2 === 0,
        'container-image ms-lg-5': index % 2 !== 0
      }"
    >
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
    <div 
      class="col-12 col-lg-6"
      :class="{
        'ps-lg-5': index % 2 === 0,
        'pe-lg-5': index % 2 !== 0
      }"
    >
      <h2 class="mb-4 mb-lg-4 my-4 my-lg-0 title-link">
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
  computed: {
    pathimages() {
      if (process.env.NODE_ENV === 'development') {
        return process.env.VUE_APP_API_MAIN_URL_DEV;
      }
      return "https://danielmaestre.es";
    }
  }
};
</script>
