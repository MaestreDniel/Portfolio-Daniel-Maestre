<template>
  <article class="transition-1 my-5">
    <!-- <div><i class="big-icon my-5" :class="skill.title + ' ' + skill.hover"></i></div> -->
    <div class="align-self-start">
      <i class="big-icon my-5" :class="skill.title" />
    </div>
    <h2>{{ skill.description }}</h2>
  </article>
</template>

<script>
export default {
  name: "SkillItem",
  props: {
    skill: Object
  }
};
</script>
