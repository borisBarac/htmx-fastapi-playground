import { useLocalStorage, type RemovableRef } from '@vueuse/core'
import { onMounted, onUnmounted } from 'vue'
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

  const codeStorage = useLocalStorage<string>(codePath, '')
  const editorStorage = useLocalStorage<string | null>(editorPath, '')

  const stateIsValid = (state: EditState): boolean => {
    return (state.code?.length ?? 0 > 0) ? true : false
  }

  const save = (state: EditState): void => {
    if (stateIsValid(state) === false) return

    editorStorage.value = state.editorState
    codeStorage.value = state.code
  }

  const get = (): EditState | null => {
    const code = codeStorage.value
    const editState = editorStorage.value

    if (code.length > 0) {
      return { code, editorState: editState }
    } else {
      return null
    }
  }

  return { get, save }
}

type ChangeListener = ((timeCalled: number, state?: string) => void) | null

const useWatchEditorStorage = (
  lang: CodeLanguages,
  editorId: string,
  checkEverySeconds: number,
  changeListener: ChangeListener
) => {
  const codePath = codeStoragePathFor(lang) + '_' + editorId
  const codeStorage = useLocalStorage<string>(codePath, '')

  let interval: NodeJS.Timeout
  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  let lastCheckTime: number
  let lastUpdateStr: string | null

  onMounted(() => {
    interval = setInterval(() => {
      if (codeStorage.value === lastUpdateStr) return

      lastUpdateStr = codeStorage.value
      lastCheckTime = new Date().getTime()
      changeListener?.(lastCheckTime, lastUpdateStr)
    }, checkEverySeconds * 1000)
  })
  onUnmounted(() => {
    // Don't forget to remove the interval before destroying the component
    clearInterval(interval)
  })
}

const useLocalStorageRef = (lang: CodeLanguages, editorId: string): RemovableRef<string> => {
  const codePath = codeStoragePathFor(lang) + '_' + editorId
  return useLocalStorage<string>(codePath, '')
}

export { useEditorStorage, useWatchEditorStorage, useLocalStorageRef }
