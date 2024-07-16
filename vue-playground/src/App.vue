<script setup lang="ts"></script>

<template class="template">
  <div class="template container">
    <div style="background-color: aqua" class="item">1111</div>
    <div style="background-color: yellow" class="item">22222</div>
    <div style="background-color: orange" class="item">333333</div>
  </div>
</template>

<style scoped>
.template {
  width: 100%;
  height: 100%;
}

.container {
  display: flex;
  justify-content: center;
  align-items: stretch;
  align-content: center;
}

.item {
  flex-grow: 1;
  flex-basis: auto;
  align-self: auto;
}
</style>
