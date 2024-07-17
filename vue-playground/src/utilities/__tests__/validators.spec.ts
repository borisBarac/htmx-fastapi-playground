import { describe, it, expect } from 'vitest'
import { isValidJSON, isValidHTMLTag } from '../validators'

describe('Validation functions', () => {
  it('should identify valid JSON', () => {
    const validObject = JSON.stringify({ name: 'John', age: 30 })
    expect(isValidJSON(validObject)).toBe(true)
  })

  it('should identify invalid JSON', () => {
    const invalidObject = 'This is not JSON'
    expect(isValidJSON(invalidObject)).toBe(false)
  })

  it('should identify valid and invalid HTML', () => {
    const str1 = "<input value = '>'>"
    expect(isValidHTMLTag(str1)).toBe(true)

    const str2 = '<br/>'
    expect(isValidHTMLTag(str2)).toBe(true)

    const str3 = 'br/>'
    expect(isValidHTMLTag(str3)).toBe(false)

    const str4 = "<'br/>"
    expect(isValidHTMLTag(str4)).toBe(false)
  })
})
