<template>
  <span id="typewriter" class="caret" />
</template>

<script>
import typewriterItem from "@/locales/es/components/typewriter.item";
export default {
  name: "TypewriterItem",
  data() {
    return {
      i: 0,
      key: 0,
      typingInterval: null,
      deleteInterval: null
    }
  },
  computed: {
    keywordsList() {
      const messages = Object.keys(typewriterItem);
      let keywords = [];
      messages.forEach(key => {
        keywords.push(this.$t(`typewriterItem.${key}`))
      });
      return keywords;
    }
  },
  mounted() {
    setTimeout(() => {
      this.typingInterval = setInterval(this.typing, 150);
      this.deleteInterval = setInterval(this.clear, 5000);
    }, 1000);
  },
  unmounted() {
    clearInterval(this.typingInterval);
    clearInterval(this.deleteInterval);
  },
  methods: {
    typing() {
      let keyword = this.keywordsList[this.key];
      if (this.i < keyword.length) {
        document.getElementById("typewriter").innerHTML += keyword.charAt(this.i);
        this.i++;
      }
    },
    clear() {
      this.key = (this.key + 1) % this.keywordsList.length;
      document.getElementById("typewriter").innerHTML = "";
      this.i = 0;
    }
  } 
};
</script>