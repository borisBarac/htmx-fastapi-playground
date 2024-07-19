<script setup lang="ts">
import PannelContainer from './components/playground/PannelContainer.vue'
import CodeEditor from './components/playground/CodeEditor/CodeEditor.vue'
import HtmxRenderer from './components/playground/HtmxRenderer/HtmxRenderer.vue'
import type { PanelItem } from './components/playground/PannelContainer.vue'
import type { TupleArray } from './components/playground/HtmxRenderer/HtmxRenderer'
import { ProviderEvents } from '@/consts'

const items: PanelItem[] = [
  {
    id: 'json_e_1',
    panelType: 'editor',
    codeLanguage: 'json'
  },
  {
    id: 'html_e_1',
    panelType: 'editor',
    codeLanguage: 'html'
  },
  {
    id: 'web_r_1',
    panelType: 'preview',
    codeLanguage: undefined
  }
]

const renderItems: TupleArray = (
  items.filter((item) => item.panelType === 'editor' && item.codeLanguage) ?? []
).map((item) => [item.codeLanguage ?? 'json', item.id])
</script>

<template>
  <PannelContainer :items="items" class="full-fill">
    <template #item="{ id, panelType, codeLanguage }">
      <CodeEditor
        v-if="codeLanguage && panelType === 'editor'"
        :language="codeLanguage!"
        :editorId="id"
      />
      <HtmxRenderer
        v-else
        :urlEventKey="ProviderEvents.Reload"
        :minSecDebounce="1"
        :maxSecDebounce="5"
        :editorItems="renderItems"
      />
    </template>
  </PannelContainer>
</template>

<style scoped>
.full-fill {
  width: 100%;
  height: 100%;
  background-color: blueviolet;
}
</style>
