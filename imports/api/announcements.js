import { Meteor } from 'meteor/meteor'
import { Mongo } from 'meteor/mongo'

export const AnnouncementsCollection = new Mongo.Collection('announcements')

if (Meteor.isServer) {
  Meteor.publish('announcements', function () {
    return AnnouncementsCollection.find({})
  })
}