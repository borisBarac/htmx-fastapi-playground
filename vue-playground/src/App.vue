<script setup lang="ts">
import PannelContainer from './components/playground/PannelContainer.vue'
import CodeEditor from './components/playground/CodeEditor/CodeEditor.vue'
import HtmxRenderer from './components/playground/HtmxRenderer/HtmxRenderer.vue'
import NavBar from './components/NavBar.vue'
import type { PanelItem } from './components/playground/PannelContainer.vue'
import type { TupleArray } from './components/playground/HtmxRenderer/HtmxRenderer'
import { ProviderEvents } from '@/consts'
import { computed, provide, ref } from 'vue'
import { useWindowSize } from '@vueuse/core'

const { width, height } = useWindowSize()

const screenSizeSupported = computed(
  () => width.value > height.value * 1.2 && height.value > 0 && width.value > 560
)

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

// set up the Reload Render provider
const renderItems: TupleArray = (
  items.filter((item) => item.panelType === 'editor' && item.codeLanguage) ?? []
).map((item) => [item.codeLanguage ?? 'json', item.id])

const providerReloadKey = ProviderEvents.Reload
const lastRenderTime = ref(Date.now())
provide(providerReloadKey, lastRenderTime)
</script>

<template>
  <NavBar class=".nav-bar" />
  <div v-if="screenSizeSupported" class="full-fill">
    <p class="instruction">Just start typing, reload is automatic</p>
    <PannelContainer :items="items" class="full-fill">
      <template #item="{ id, panelType, codeLanguage }">
        <CodeEditor
          v-if="codeLanguage && panelType === 'editor'"
          :language="codeLanguage!"
          :editorId="id"
        />
        <HtmxRenderer
          v-else
          :urlEventKey="providerReloadKey"
          :minSecDebounce="1"
          :maxSecDebounce="5"
          :editorItems="renderItems"
        />
      </template>
    </PannelContainer>
  </div>
  <div v-else class="full-fill">
    <h3 class="not-supported">Sceeen not supported</h3>
  </div>
</template>

<style scoped>
.full-fill {
  width: 100%;
  height: 100%;
}

.instruction {
  padding: 0.2rem;
}

.nav-bar {
  padding-bottom: 0.5rem;
}

.not-supported {
  align-content: center;
  text-align: center;
  height: 100%;
}
</style>
