<script setup lang="ts">
import { inject, onMounted, onUnmounted, ref, type Ref } from 'vue'
import { useDebounceFn, useResizeObserver } from '@vueuse/core'
import * as monaco from 'monaco-editor'

import { editorTheme, getWorker, initalEditorValue } from './CodeEditor'
import { ProviderEvents, type CodeLanguages } from '@/consts'
import { useEditorStorage } from '@/compositions/storage'

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

const reloadProviderRef = inject<Ref<number>>(ProviderEvents.Reload)

const setReloadProvider = () => {
  if (reloadProviderRef) {
    reloadProviderRef.value = Date.now()
  }
}

const { get: getStorageState, save: saveStorageState } = useEditorStorage(
  props.language,
  props.editorId
)

const loadCodeFromStorage = () => {
  const initCode = initalEditorValue(props.language)
  const currentCode = getStorageState()?.code ?? initCode
  editor.setValue(currentCode)
}

const saveCodeAndEmitChange = () => {
  const current = getStorageState()
  if (current?.code !== editor.getValue()!) {
    saveStorageState({ code: editor.getValue(), editorState: null })
    emit('change', editor.getValue())
    setReloadProvider()
  }
}

onMounted(() => {
  editor = monaco.editor.create(container.value!, {
    language: props.language,
    theme: editorTheme
  })

  emit('change', getStorageState()?.code ?? '')

  editor.onDidChangeModelContent(
    // we update the values in storage on change
    useDebounceFn(() => {
      saveCodeAndEmitChange()
    }, 500)
  )

  loadCodeFromStorage()
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
  <div ref="container" style="height: 100%" />
</template>
