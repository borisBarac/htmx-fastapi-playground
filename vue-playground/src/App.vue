<script setup lang="ts">
import CodeEditor from './components/playground/CodeEditor/CodeEditor.vue'
</script>

<template class="template">
  <CodeEditor class="code-editor" language="json" editorId="1" />
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
