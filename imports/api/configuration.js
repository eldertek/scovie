import { Meteor } from 'meteor/meteor'
import { Mongo } from 'meteor/mongo'

export const ConfigurationCollection = new Mongo.Collection('configuration')

if (Meteor.isServer) {
  Meteor.publish('configuration', function () {
    return ConfigurationCollection.find({})
  })
}