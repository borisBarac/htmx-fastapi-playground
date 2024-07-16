import { useStorage } from '@vueuse/core'
import type { CodeLanguages } from '@/consts'

type StoragePath = 'local_storage_json' | 'local_storage_html'

const editorStatePath = 'local_storage_editor'

const codeStoragePathFor = (lang: CodeLanguages): StoragePath => {
  switch (lang) {
    case 'json':
      return 'local_storage_json'
    case 'html':
      return 'local_storage_html'
  }
}

const useEditorStorage = (lang: CodeLanguages, editorId: string) => {
  const codePath = codeStoragePathFor(lang) + '_' + editorId
  const editorPath = editorStatePath + '_' + editorId

  type EditState = { code: string | null; editorState: string | null }

  const editorStorage = useStorage(editorPath, '')
  const codeStorage = useStorage(codePath, '')

  const save = (state: EditState): void => {
    editorStorage.value = state.editorState
    codeStorage.value = state.code
  }

  const get = (): EditState | null => {
    const code = codeStorage.value
    const editState = editorStorage.value

    if (code.length > 0 && editState.length > 0) {
      return { code, editorState: editState }
    } else {
      return null
    }
  }

  return { get, save }
}

export default useEditorStorage
