<script setup lang="ts">
import IconEcosystem from './icons/IconEcosystem.vue'
import PythonIcon from './icons/PythonIcon.vue'
</script>

<template>
  <div class="nav">
    <div class="iconPadding"><IconEcosystem /></div>
    <div class="iconPadding"><PythonIcon /></div>
    <h2>FastiApi / Jinja Template State Rendered Playground</h2>
    <a href="https://jinja.palletsprojects.com/en/3.1.x/"> Jinja DOCS </a>
  </div>
</template>

<style scoped>
h2 {
  color: var(--neo-green);
  padding: 0.5cap;
  font-weight: bold;
}

a {
  margin-left: auto;
  padding: 0.5rem;
}

a {
  color: var(--color-text-soft);
}

.iconPadding {
  padding: 0.5rem;
}

.nav {
  background-color: var(--color-background-soft);
  width: 100%;
  height: 70px;
  display: flex;
  flex-direction: row;
  align-items: center;
}
</style>

<script setup></script>
