<script setup lang="ts">
import { onMounted, onUnmounted, ref } from 'vue'
import { useDebounceFn, useResizeObserver } from '@vueuse/core'
import * as monaco from 'monaco-editor'

import { editorTheme, getWorker, initalEditorValue } from './CodeEditor'
import type { CodeLanguages } from '@/consts'
import useEditorStorage from '@/compositions/storage'

interface Props {
  language: CodeLanguages
  editorId: string
}
const props = defineProps<Props>()

const container = ref<HTMLDivElement | null>(null)
let editor: monaco.editor.IStandaloneCodeEditor

// https://github.com/vitejs/vite/discussions/1791
self.MonacoEnvironment = { getWorker: getWorker }
const emit = defineEmits<(e: 'change', payload: string) => void>()

const { get: getStorageState, save: saveStorageState } = useEditorStorage(
  props.language,
  props.editorId
)

onMounted(() => {
  editor = monaco.editor.create(container.value!, {
    language: props.language,
    theme: editorTheme
  })

  emit('change', getStorageState()?.code ?? initalEditorValue(props.language))

  editor.onDidChangeModelContent(
    // we update the values in storage on change
    useDebounceFn(() => {
      const current = getStorageState()
      if (current?.code !== editor.getValue()!) {
        saveStorageState({ code: editor.getValue(), editorState: null })
        emit('change', editor.getValue())
      }
    }, 500)
  )

  const current = getStorageState()
  if (current?.code) {
    editor.setValue(current.code)
  }
})

const editorObserver = useResizeObserver(container, () => {
  editor.layout()
})

onUnmounted(() => {
  editor?.dispose()
  editorObserver.stop()
})
</script>

<template>
  <div ref="container" style="height: calc(100% - 2.5rem)" />
</template>
