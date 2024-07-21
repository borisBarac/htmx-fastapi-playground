<script setup lang="ts">
import { inject, ref } from 'vue'
import { watchDebounced } from '@vueuse/core'
import { initUrl, useStorageToGetUrl, type TupleArray } from './HtmxRenderer'

interface Props {
  urlEventKey: string
  minSecDebounce: number
  maxSecDebounce: number
  editorItems: TupleArray | undefined
}
const props = defineProps<Props>()
const urlChangeEventKey: any = inject(props.urlEventKey)

var deboundedUrl = ref(initUrl)
var reloadCount = ref(0)

const reloadIframe = () => {
  const len = props.editorItems?.length ?? 2
  if (len < 2) return
  const newUrl = useStorageToGetUrl(props.editorItems!)
  deboundedUrl.value = newUrl
}

watchDebounced(
  urlChangeEventKey,
  () => {
    reloadCount.value = reloadCount.value + 1

    reloadIframe()
  },
  { debounce: props.minSecDebounce * 1000, maxWait: props.maxSecDebounce * 1000 }
)
</script>

<template>
  <div class="container">
    <!-- <h2>{{ reloadCount }}</h2>
    <h2>{{ deboundedUrl }}</h2> -->
    <embed class="item" :src="deboundedUrl" scrolling="yes" />
  </div>
</template>

<style scoped>
.container {
  width: 100%;
  height: 100%;
  background-color: var(--color-background-soft);
}

.item {
  width: 100%;
  height: 100%;
}

embed {
  overflow: scroll !important;
  pointer-events: none !important;
}
</style>
