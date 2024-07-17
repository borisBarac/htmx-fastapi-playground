<script setup lang="ts">
import { inject, ref } from 'vue'
import { watchDebounced } from '@vueuse/core'

interface Props {
  urlEventKey: string
  minSecDebounce: number
  maxSecDebounce: number
}
const props = defineProps<Props>()
const iFrameUrl: any = inject(props.urlEventKey)

var deboundedUrl = ref('')
var reloadCount = ref(0)

watchDebounced(
  iFrameUrl,
  () => {
    reloadCount.value = reloadCount.value + 1
    deboundedUrl.value = iFrameUrl.value
  },
  { debounce: props.minSecDebounce * 1000, maxWait: props.maxSecDebounce * 1000 }
)
</script>

<template>
  <div class="fit-w-h">
    <!-- <h2>{{ reloadCount }}</h2>
    <h2>{{ deboundedUrl }}</h2> -->
    <iframe class="fit-w-h" :src="deboundedUrl" frameborder="0" scrolling="yes" />
  </div>
</template>

<style scoped>
.fit-w-h {
  width: 100%;
  height: 100%;
}
</style>
