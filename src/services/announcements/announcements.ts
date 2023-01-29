// For more information about this file see https://dove.feathersjs.com/guides/cli/service.html

import { hooks as schemaHooks } from '@feathersjs/schema'

import {
  announcementDataValidator,
  announcementPatchValidator,
  announcementQueryValidator,
  announcementResolver,
  announcementExternalResolver,
  announcementDataResolver,
  announcementPatchResolver,
  announcementQueryResolver
} from './announcements.schema'

import type { Application } from '../../declarations'
import { AnnouncementService, getOptions } from './announcements.class'

export * from './announcements.class'
export * from './announcements.schema'

// A configure function that registers the service and its hooks via `app.configure`
export const announcement = (app: Application) => {
  // Register our service on the Feathers application
  app.use('announcements', new AnnouncementService(getOptions(app)), {
    // A list of all methods this service exposes externally
    methods: ['find', 'get', 'create', 'patch', 'remove'],
    // You can add additional custom events to be sent to clients here
    events: []
  })
  // Initialize hooks
  app.service('announcements').hooks({
    around: {
      all: [
        schemaHooks.resolveExternal(announcementExternalResolver),
        schemaHooks.resolveResult(announcementResolver)
      ]
    },
    before: {
      all: [
        schemaHooks.validateQuery(announcementQueryValidator),
        schemaHooks.resolveQuery(announcementQueryResolver)
      ],
      find: [],
      get: [],
      create: [
        schemaHooks.validateData(announcementDataValidator),
        schemaHooks.resolveData(announcementDataResolver)
      ],
      patch: [
        schemaHooks.validateData(announcementPatchValidator),
        schemaHooks.resolveData(announcementPatchResolver)
      ],
      remove: []
    },
    after: {
      all: []
    },
    error: {
      all: []
    }
  })
}

// Add this service to the service type index
declare module '../../declarations' {
  interface ServiceTypes {
    announcements: AnnouncementService
  }
}
