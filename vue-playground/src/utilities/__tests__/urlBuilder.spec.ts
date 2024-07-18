import { describe, it, expect } from 'vitest'
import { buldWebPathFor, IframeRoute, Endpoints } from '../urlBuilder'

describe('URLBuilder', () => {
  it('should return the correct URL with query string', () => {
    const queryParams = {
      a: 'b',
      c: 'd'
    }
    const route = IframeRoute(Endpoints.root, queryParams)
    expect(buldWebPathFor(route)).toBe(`http://localhost:8000/?a=b&c=d`)
  })
  it('should return the correct URL without query string', () => {
    const route = IframeRoute(Endpoints.render, {})
    expect(buldWebPathFor(route)).toBe(`http://localhost:8000/render`)
  })
  it('should return the correct URL without query string and path', () => {
    const queryParams = {
      a: 'b',
      c: 'd'
    }
    const route = IframeRoute(Endpoints.render, queryParams)
    expect(buldWebPathFor(route)).toBe(`http://localhost:8000/render?a=b&c=d`)
  })
})
