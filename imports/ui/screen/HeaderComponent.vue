<template>
  <nav class="navbar bg-warning">
    <div class="container-fluid">
      <span class="navbar-brand mb-0 text-start" style="font-size: 3vh;">
        {{ enterpriseName }}
      </span>
      <span id="time" class="navbar-brand mb-0 text-end" style="font-size: 3vh;">
        {{ enterpriseTime }}
      </span>
    </div>
  </nav>
</template>
<script>
// Import axios for HTTP requests
import axios from 'axios'
// Export the component
export default {
  // The component's name
  name: "HeaderComponent",
  // The component's data
  data() {
    // Return the data
    return {
      // The enterprise name
      enterpriseName: "",
      // The enterprise time
      enterpriseTime: ""
    }
  },
  // The component's methods
  methods: {
    // Fetch the configuration
    fetchConfiguration() {
      // Get the configuration
      axios.get('http://localhost:3000/api/configuration')
        .then(response => {
          this.enterpriseName = response.data.find(o => o.name === 'enterprise_name').value;
        })
        .catch(error => {
          console.log(error);
        })
    },
  },
  // The component's mounted hook
  mounted() {
    // Fetch the configuration
    this.fetchConfiguration();
    setInterval(() => {
      this.fetchConfiguration();
    }, 1000 * 60 * 5);
    // Set the enterprise time
    setInterval(() => {
      this.enterpriseTime = new Date().toLocaleString('fr-FR', {
        weekday: 'long',
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: 'numeric',
        minute: 'numeric',
        second: 'numeric',
        hour12: false
      });
      this.enterpriseTime = this.enterpriseTime.charAt(0).toUpperCase() + this.enterpriseTime.slice(1);
    }, 1000);
  }
}
</script>