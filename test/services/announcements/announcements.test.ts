// For more information about this file see https://dove.feathersjs.com/guides/cli/service.test.html
import assert from 'assert'
import { app } from '../../../src/app'

describe('announcements service', () => {
  it('registered the service', () => {
    const service = app.service('announcements')

    assert.ok(service, 'Registered the service')
  })
})
