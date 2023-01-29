import { Meteor } from 'meteor/meteor'
import { createApp } from 'vue'
import { VueMeteor } from 'vue-meteor-tracker'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap.js'

import App from './App.vue'

Meteor.startup(() => {
  const app = createApp(App)
  app.use(VueMeteor)
  app.mount('#app')
})
