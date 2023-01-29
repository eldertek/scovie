import { Meteor } from 'meteor/meteor'
import { Mongo } from 'meteor/mongo'

export const TimesCollection = new Mongo.Collection('times')

if (Meteor.isServer) {
  Meteor.publish('times', function () {
    return TimesCollection.find({})
  })
}