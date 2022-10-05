import { mount } from '@vue/test-utils'
import Example from '@/components/Example.vue'

describe('Example', () => {
  test('whatever', () => {
    const wrapper = mount(Example)
    expect(wrapper.vm).toBeTruthy()
  })
})
