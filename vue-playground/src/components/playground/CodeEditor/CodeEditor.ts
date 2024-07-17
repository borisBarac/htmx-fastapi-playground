import EditorWorker from 'monaco-editor/esm/vs/editor/editor.worker?worker'
import JSONWorker from 'monaco-editor/esm/vs/language/json/json.worker?worker'
import HTMLWorker from 'monaco-editor/esm/vs/language/html/html.worker?worker'
import { initJson, initHtml } from '@/consts'

import type { CodeLanguages, MonacoThemesEnum } from '@/consts'

const editorTheme: MonacoThemesEnum = 'vs-dark'

const initalEditorValue = (lang: CodeLanguages): string => {
  switch (lang) {
    case 'json':
      return initJson
    case 'html':
      return initHtml
  }
}

// https://github.com/vitejs/vite/discussions/1791
const getWorker = (_: string, label: string) => {
  switch (label) {
    case 'json':
      return new JSONWorker()
    case 'html':
      return new HTMLWorker()
    default:
      return new EditorWorker()
  }
}

export { editorTheme, initalEditorValue, getWorker }
