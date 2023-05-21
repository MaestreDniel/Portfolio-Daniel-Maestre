<template>
  <div class="row gx-5">
    <div class="col-12 col-lg-6">
      <h2 class="mb-3">
        {{ work.title }}
      </h2>
      <div class="title-link my-4 fs-5">
        <a
          :href="work.url"
          target="_blank"
          rel="noreferrer noopener"
        >
          {{ work.company }}
          <i class="fa-solid fa-arrow-up-right-from-square mx-2" />
        </a>
      </div>
      <p class="card-text opacity-80 me-0 me-lg-5">
        {{ work.content }}
      </p>
    </div>
    <div class="col-12 col-lg-6">
      <svg height="20" width="10" class="d-none d-lg-block position-absolute start-50 translate-middle-x">
        <circle 
          cx="5" 
          cy="14" 
          r="5" 
          fill="#edfcfe" 
          stroke="#212121" 
          stroke-width="1"
        />
      </svg>
      <span class="ms-0 ms-lg-3">
        {{ work.start_date }} - {{ work?.finish_date ?? "actualmente" }}
      </span>
    </div>
  </div>
</template>

<script>
export default {
  name: "WorkItem",
  props: {
    work: {
      type: Object,
      required: true
    },
    index: {
      type: Number,
      required: true
    }
  }
};
</script>
