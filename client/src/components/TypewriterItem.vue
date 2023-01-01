<template>
  <h1 class="col-12 typewriter my-3">
    {{ text }}
  </h1>
</template>

<script>
  export default {
  name: "TypewriterItem",
  props: {
    text: {
      type: String,
      default: "Tus ideas: desde tu mente hasta la web."
    }
  }
};
</script>