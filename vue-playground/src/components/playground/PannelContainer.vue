<script setup lang="ts">
import { onMounted } from 'vue'
import Split from 'split.js'

onMounted(() => {
  Split(['#panel-1', '#panel-2', '#panel-3'])
})
</script>

<template>
  <div class="template container">
    <div id="panel-1" style="background-color: aqua" class="item"></div>
    <div id="panel-2" style="background-color: yellow" class="item"></div>
    <div id="panel-3" style="background-color: orange" class="item"></div>
  </div>
</template>

<style scoped>
.container {
  display: flex;
  justify-content: center;
  align-items: stretch;
  align-content: center;
}

.item {
  margin: 0.5rem;
  flex-grow: 1;
  flex-basis: auto;
  align-self: auto;
}

.split {
  display: flex;
  flex-direction: row;
}
</style>
