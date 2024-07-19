<script setup lang="ts">
import Splitter from 'primevue/splitter'
import SplitterPanel from 'primevue/splitterpanel'

import type { CodeLanguages, PanelType } from '@/consts'

export type PanelItem = {
  id: string
  panelType: PanelType
  codeLanguage: CodeLanguages | undefined
}

defineProps<{
  items?: PanelItem[]
}>()
</script>

<template>
  <Splitter class="container">
    <SplitterPanel v-for="item in items" :key="item.id" class="panel">
      <slot name="item" v-bind="item" />
    </SplitterPanel>
  </Splitter>
</template>

<style scoped>
.container {
  background-color: aqua;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: stretch;
  align-content: center;
}

.panel {
  margin: 0.25rem;
  flex-grow: 1;
  flex-basis: auto;
  align-self: auto;
}

.split {
  display: flex;
  flex-direction: row;
}
</style>
