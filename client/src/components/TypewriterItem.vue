<template>
  <h1 class="col-12 col-sm-9 my-3">
    {{ slogan }}
    <span class="typewriter">
      {{ text }}
    </span>
  </h1>
</template>

<script>
  export default {
  name: "TypewriterItem",
  props: {
    slogan: {
      type: String,
      required: true
    },
    text: {
      type: String,
      required: true
    }
  }
};
</script>