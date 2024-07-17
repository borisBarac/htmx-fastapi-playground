<script setup lang="ts">
import HtmxRenderer from './components/playground/HtmxRenderer.vue'
import { ProviderEvents } from './consts'

import { ref, provide } from 'vue'

// by providing a ref, the GrandChild
// can react to changes happening here.
const bind_val = ref('www.google.com')
provide(ProviderEvents.Reload, bind_val)
</script>

<template class="template">
  <input v-model="bind_val" />

  <HtmxRenderer
    class="code-editor"
    :urlEventKey="ProviderEvents.Reload"
    :minSecDebounce="1"
    :maxSecDebounce="5"
  />
</template>

<style scoped>
.template {
  /* width: 100%; */
  height: 100%;
}

.code-editor {
  width: 100%;
  height: 100%;
}
</style>

<script setup></script>
