<script setup lang="ts">
import { inject, watch } from 'vue'

interface Props {
  urlEventKey: string
}
const props = defineProps<Props>()
const iFrameUrl: string = inject(props.urlEventKey)

watch(shouldReload, () => {
  iframe.src = { iFrameUrl }
})
</script>

<template>
  <div>
    <h2>My Iframe</h2>
    <iframe frameborder="0" scrolling="yes"></iframe>
  </div>
</template>

<style scoped>
/* Add any styles for the iframe container here */
iframe {
  width: 100%;
  height: 400px; /* Adjust height as needed */
}
</style>
