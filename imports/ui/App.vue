<template>
  <div class="bg-black">
    <div v-if="screenMode === 'announcements-planning'">
      <HeaderComponent></HeaderComponent>
      <AnnouncementsComponent></AnnouncementsComponent>
      <PlanningComponent></PlanningComponent>
      <FooterComponent></FooterComponent>
    </div>
    <div v-if="screenMode === 'caroussel'">
      <CarousselComponent></CarousselComponent>
    </div>
    <div v-if="screenMode === 'all'">
      <div class="row">
        <div class="col pe-0">
          <HeaderComponent></HeaderComponent>
          <AnnouncementsComponent></AnnouncementsComponent>
          <PlanningComponent></PlanningComponent>
        </div>
        <div class="col">
          <CarousselComponent></CarousselComponent>
        </div>
        <FooterComponent></FooterComponent>
      </div>
    </div>
    <div v-if="screenMode === 'valentine'">
      <ValentineDayComponent></ValentineDayComponent>
    </div>
  </div>
</template>
<script>
// Components
import HeaderComponent from './screen/header.vue'
import AnnouncementsComponent from './screen/announcement.vue'
import PlanningComponent from './screen/planning.vue'
import CarousselComponent from './screen/caroussel.vue'
import FooterComponent from './screen/footer.vue'

// Events
import ValentineDayComponent from './events/valentine.vue'

export default {
  name: 'App',
  data() {
    return {
      screenMode: 'announcements-planning'
    }
  },
  components: {
    // Components
    HeaderComponent,
    AnnouncementsComponent,
    PlanningComponent,
    CarousselComponent,
    FooterComponent,

    // Events
    ValentineDayComponent
  },
  created() {
    // Remove cursor
    document.body.style.cursor = 'none';
    // Add bg-black class to body
    document.body.classList.add('bg-black');

    // Change screen mode every 15 seconds
    setInterval(() => {
      const today = new Date();

      // Create a list of all screen modes
      const screenModes = [
        'announcements-planning',
        'caroussel',
      ];

      // Add all screen mode only to desktop
      if (window.innerWidth > 767) {
        screenModes.push('all');
      }

      // Add valentine day to screen modes
      if (today.getMonth() === 1 && today.getDate() === 14 && !screenModes.includes('valentine')) {
        // Add valentine day to the list of screen modes
        screenModes.push('valentine');
      } else if (today.getMonth() === 1 && today.getDate() !== 14 && screenModes.includes('valentine')) {
        // Remove valentine day from the list of screen modes
        screenModes.splice(screenModes.indexOf('valentine'), 1);
      }

      this.screenMode = screenModes[(screenModes.indexOf(this.screenMode) + 1) % screenModes.length];
    }, 15000);
  }
}
</script>