export const mergeRecords = (records: Record<string, string>[]): Record<string, string> => {
  const mergedRecord: Record<string, string> = {}

  for (const record of records) {
    Object.assign(mergedRecord, record)
  }

  return mergedRecord
}

export const getSessionId = (): string => {
  const uniqueId = () => {
    const dateString = Date.now().toString(36)
    const randomness = Math.random().toString(36).substr(2)
    return dateString + randomness
  }

  const key = 'session_id_address'

  if (localStorage.getItem(key)?.length ?? 0 > 12) {
    return localStorage.getItem(key)!
  } else {
    const newId = uniqueId()
    localStorage.setItem(key, newId)
    return newId
  }
}
