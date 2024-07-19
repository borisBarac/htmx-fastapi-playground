import { useLocalStorageRef } from '@/compositions/storage'
import { CodeLangApiParamMap, type CodeLanguages } from '@/consts'
import { encodeBase64 } from '@/utilities/base64encoder'
import { getMAC, mergeRecords } from '@/utilities/helper'
import { buldWebPathFor, Endpoints, IframeRoute } from '@/utilities/urlBuilder'
import { assert } from 'console'

export type TupleArray = Array<[CodeLanguages, string]>
export const initUrl = buldWebPathFor(IframeRoute(Endpoints.root, {}))

const useStorageToGetUrl = (items: TupleArray): string => {
  const encodedValues = items.map((item) => {
    const storedString = useLocalStorageRef(item[0], item[1]).value
    return encodeBase64(storedString)
  })

  assert(encodedValues.length === items.length)

  const query: Record<string, string> = mergeRecords(
    items.map((item, index) => {
      const lang: CodeLanguages = item[0]
      const apiParamName = CodeLangApiParamMap[lang]

      return { [apiParamName]: encodedValues[index] } as const
    })
  )

  query['mac_address'] = getMAC()
  query['epoch_time'] = Math.floor(Date.now() / 1000).toString()

  return buldWebPathFor(IframeRoute(Endpoints.render, query))
}

export { useStorageToGetUrl }
