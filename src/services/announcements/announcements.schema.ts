// // For more information about this file see https://dove.feathersjs.com/guides/cli/service.schemas.html
import { resolve } from '@feathersjs/schema'
import { Type, getDataValidator, getValidator, querySyntax } from '@feathersjs/typebox'
import type { Static } from '@feathersjs/typebox'

import type { HookContext } from '../../declarations'
import { dataValidator, queryValidator } from '../../validators'

// Main data model schema
export const announcementSchema = Type.Object(
  {
    id: Type.Number(),
    type: Type.String(),   
    text: Type.String()
  },
  { $id: 'Announcement', additionalProperties: false }
)
export type Announcement = Static<typeof announcementSchema>
export const announcementResolver = resolve<Announcement, HookContext>({})

export const announcementExternalResolver = resolve<Announcement, HookContext>({})

// Schema for creating new entries
export const announcementDataSchema = Type.Pick(announcementSchema, ['type', 'text'], {
  $id: 'AnnouncementData'
})
export type AnnouncementData = Static<typeof announcementDataSchema>
export const announcementDataValidator = getDataValidator(announcementDataSchema, dataValidator)
export const announcementDataResolver = resolve<Announcement, HookContext>({})

// Schema for updating existing entries
export const announcementPatchSchema = Type.Partial(announcementDataSchema, {
  $id: 'AnnouncementPatch'
})
export type AnnouncementPatch = Static<typeof announcementPatchSchema>
export const announcementPatchValidator = getDataValidator(announcementPatchSchema, dataValidator)
export const announcementPatchResolver = resolve<Announcement, HookContext>({})

// Schema for allowed query properties
export const announcementQueryProperties = Type.Pick(announcementSchema, ['id', 'type', 'text'])
export const announcementQuerySchema = Type.Intersect(
  [
    querySyntax(announcementQueryProperties),
    // Add additional query properties here
    Type.Object({}, { additionalProperties: false })
  ],
  { additionalProperties: false }
)
export type AnnouncementQuery = Static<typeof announcementQuerySchema>
export const announcementQueryValidator = getValidator(announcementQuerySchema, queryValidator)
export const announcementQueryResolver = resolve<AnnouncementQuery, HookContext>({})
