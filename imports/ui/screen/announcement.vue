<template>
    <div>
        <nav class="navbar bg-white" style="--bs-bg-opacity: .20;">
            <div class="container-fluid justify-content-center">
                <span class="navbar-brand text-light afont-size">
                    <strong>Annonces du jour | Professeurs absents</strong>
                </span>
            </div>
        </nav>
        <table class="table table-bordered border-white table-dark table-striped sfont-size">
            <thead>
                <tr>
                    <th width="14%">Type</th>
                    <th width="86%">Message</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="announcement in visibleAnnouncements" :key="announcement.id">
                    <td>{{ announcement.type }}</td>
                    <td>{{ announcement.text }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>
<script>
// Import axios for HTTP requests
import axios from 'axios';
// Export the component
export default {
    // The component's name
    name: "AnnouncementsComponent",
    // The component's data
    data() {
        // Return the data
        return {
            // The announcements
            announcements: [],
            // The current index
            currentIndex: 0
        }
    },
    // The component's mounted hook
    mounted() {
        // Fetch the announcements
        this.fetchAnnouncements();
        setInterval(() => {
            this.fetchAnnouncements();
        }, 1000 * 60 * 5);
        // Increment the current index every 3 seconds for the visible announcements
        setInterval(() => {
            this.currentIndex = (this.currentIndex + 1) % this.announcements.length;
        }, 3000);
        // Update the max visible announcements on resize
        window.addEventListener("resize", this.updateMaxVisible);
    },
    // The component's methods
    methods: {
        // Fetch the announcements
        fetchAnnouncements() {
            // Fetch from the API
            axios.get('http://localhost:3000/api/announcements')
                .then(response => {
                    this.announcements = response.data;
                })
                .catch(error => {
                    console.log(error);
                })
        },
        // Update the max visible announcements
        updateMaxVisible() {
            this.$forceUpdate();
        }
    },
    // The component's computed properties
    computed: {
        // The visible announcements
        visibleAnnouncements() {
            return this.announcements.slice(this.currentIndex, this.currentIndex + this.maxVisible);
        },
        // The max visible announcements
        maxVisible() {
            if (window.innerWidth < 1800) {
                return 1;
            } else if (window.innerWidth < 2100) {
                return 2;
            } else if (window.innerWidth < 2400) {
                return 3;
            } else if (window.innerWidth < 2700) {
                return 4;
            } else {
                return 5;
            }
        }
    }
}
</script>
