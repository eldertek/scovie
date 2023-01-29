import { Meteor } from 'meteor/meteor'
import { Mongo } from 'meteor/mongo'

export const CarousselCollection = new Mongo.Collection('caroussel')

if (Meteor.isServer) {
  Meteor.publish('caroussel', function () {
    return CarousselCollection.find({})
  })
}