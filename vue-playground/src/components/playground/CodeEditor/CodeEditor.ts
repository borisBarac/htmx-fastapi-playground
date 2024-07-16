import EditorWorker from 'monaco-editor/esm/vs/editor/editor.worker?worker'
import JSONWorker from 'monaco-editor/esm/vs/language/json/json.worker?worker'
import HTMLWorker from 'monaco-editor/esm/vs/language/html/html.worker?worker'

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

const initJson: string = "{'fake': 'json'}"
const initHtml: string = `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>My Simple Website</title>
</head>
<body>
  <h1>Welcome to My Website</h1>
  <p>This is a simple paragraph containing some introductory text.</p>
  <ul>
    <li>Item 1 in an unordered list</li>
    <li>Item 2 in the list</li>
  </ul>
  <img src="image.jpg" alt="Image description">
  <a href="https://www.example.com">Link to another website</a>
</body>
</html>`

export { editorTheme, initalEditorValue, getWorker }
