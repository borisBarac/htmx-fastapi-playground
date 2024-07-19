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
  if (props.editorItems?.length ?? 0 < 2) return
  const newUrl = useStorageToGetUrl(props.editorItems!)
  deboundedUrl.value = newUrl
}

watchDebounced(
  urlChangeEventKey,
  () => {
    reloadCount.value = reloadCount.value + 1

    //TODO: Enamble hot reload
    // reloadIframe()
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
