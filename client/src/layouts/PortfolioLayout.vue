<template>
  <NavBar />
  <RouterView />
</template>

<script>
import NavBar from "@/components/NavBar.vue";

export default {
  name: "PortfolioLayout",
  components: {
    NavBar,
  },
};
</script>
