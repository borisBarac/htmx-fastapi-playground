import { describe, it, expect } from 'vitest'

import { mount } from '@vue/test-utils'
import HtmxRenderer from '../playground/HtmxRenderer/HtmxRenderer.vue'

describe('HtmxRenderer', () => {
  it('renders', () => {
    const wrapper = mount(HtmxRenderer, {
      props: {
        urlEventKey: 'INVALID',
        minSecDebounce: 1,
        maxSecDebounce: 5,
        editorItems: undefined
      }
    })
    expect(wrapper.html()).toContain('iframe')
  })
})
