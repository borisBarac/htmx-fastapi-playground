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
    const randomness = Math.random().toString(36)
    return dateString + randomness
  }

  const storage_key = 'session_id_address'

  if (localStorage.getItem(storage_key)?.length ?? 0 > 12) {
    return localStorage.getItem(storage_key)!
  } else {
    const newId = uniqueId()
    localStorage.setItem(storage_key, newId)
    return newId
  }
}
