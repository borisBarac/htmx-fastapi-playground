const isValidJSON = (text: string): boolean => {
  try {
    return JSON.parse(text) ? true : false
  } catch {
    return false
  }
}

const isValidHTMLTag = (rawHTML: string): boolean => {
  // Regex to check valid HTML tag.
  // eslint-disable-next-line no-useless-escape
  const regex = new RegExp(/<(\"[^\"]*\"|'[^']*'|[^'\">])*>/)

  // If the string is empty
  // return false
  if (rawHTML == null) {
    return false
  }

  return regex.test(rawHTML)
}

export { isValidJSON, isValidHTMLTag }
