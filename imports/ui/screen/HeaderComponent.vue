<template>
  <nav class="navbar bg-warning">
    <div class="container-fluid" >
      <span class="navbar-brand mb-0 text-start" style="font-size: 3vh;">
        {{ enterprise_name }}
      </span>
      <span id="time" class="navbar-brand mb-0 text-end" style="font-size: 3vh;">
        {{ enterprise_time }}
      </span>
    </div>
  </nav>
</template>
<script>
export default {
  name: "HeaderComponent",
  data() {
    return {
      enterprise_name: "Lycée Georges Brassens",
      actual_datetime: ""
    }
  },
  computed: {
    enterprise_time() {
      return this.actual_datetime.charAt(0).toUpperCase() + this.actual_datetime.slice(1);
    }
  },
  mounted() {
    setInterval(() => {
      this.actual_datetime = new Date().toLocaleString('fr-FR', {
        weekday: 'long',
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: 'numeric',
        minute: 'numeric',
        second: 'numeric',
        hour12: false
      });
    }, 1000);
  }
}
</script>


