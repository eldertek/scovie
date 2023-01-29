import { Meteor } from 'meteor/meteor'
import { Mongo } from 'meteor/mongo'

export const PlanningCollection = new Mongo.Collection('planning')

if (Meteor.isServer) {
  Meteor.publish('planning', function () {
    return PlanningCollection.find({})
  })
}