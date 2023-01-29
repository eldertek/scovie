import { Meteor } from 'meteor/meteor'
import { WebApp } from 'meteor/webapp'
import { ConfigurationCollection } from '/imports/api/configuration'
import { AnnouncementsCollection } from '/imports/api/announcements'

async function insertAnnouncement({ type, text }) {
  await AnnouncementsCollection.insertAsync({ type, text})
}

async function insertConfiguration({ name, value }) {
  await ConfigurationCollection.insertAsync({ name, value})
}

Meteor.startup(async () => {
  // Remove all data from the collections.
  await AnnouncementsCollection.removeAsync({})
  // If the Announcements collection is empty, add some data.
  if ((await AnnouncementsCollection.find().countAsync()) === 0) {
    await insertAnnouncement({
      type: 'ABSENCE',
      text: 'Le professeur de français est absent',
    })

    await insertAnnouncement({
      type: 'ABSENCE',
      text: 'Le professeur de mathématiques est absent',
    })

    await insertAnnouncement({
      type: 'ABSENCE',
      text: 'Le professeur d\'anglais est absent',
    })

    await insertAnnouncement({
      type: 'ABSENCE',
      text: 'Le professeur de physique est absent',
    })
  }
  
  // Remove all data from the collections.
  await ConfigurationCollection.removeAsync({})
  // If the configuration collection is empty, add some data.
  if ((await ConfigurationCollection.find().countAsync()) === 0) {
    await insertConfiguration({
      name: 'enterprise_name',
      value: 'Lycée Georges Brassens',
    }),
    await insertConfiguration({
      name: 'enterprise_time',
      value: new Date().toLocaleString('fr-FR', {
        weekday: 'long',
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: 'numeric',
        minute: 'numeric',
        second: 'numeric',
        hour12: false
      }),
    })
  }
})

WebApp.connectHandlers.use('/api/configuration', (req, res) => {
  res.writeHead(200)
  res.end(JSON.stringify(ConfigurationCollection.find().fetch()))
});

WebApp.connectHandlers.use('/api/announcements', (req, res) => {
  res.writeHead(200)
  res.end(JSON.stringify(AnnouncementsCollection.find().fetch()))
});