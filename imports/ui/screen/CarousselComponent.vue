<template>
    <div class="carousel slide carousel-fade" data-bs-ride="carousel">
        <div class="carousel-inner">
            <div class="carousel-item" v-for="(media, index) in medias" :key="index" :class="{ active: index === activeIndex }">
                <img :src="media.image" style="height: 100vh; width: 100%; object-fit: cover;" :alt="media.name" data-bs-interval="1500"  />
            </div>
        </div>
    </div>
</template>
<script>
// Import axios for HTTP requests
import axios from 'axios';
// Export the component
export default {
    // The component's name
    name: "CarouselComponent",
    // The component's data
    data() {
        // Return the data
        return {
            // The media active index
            activeIndex: 0,
            medias: []
        }
    },
    // The component's methods
    methods: {
        // Fetch the caroussel medias
        fetchCaroussel() {
            // Fetch from the API
            axios.get('http://localhost:3000/api/caroussel')
                .then(response => {
                    this.medias = response.data;
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
    // The component's mounted hook
    mounted() {
        // Fetch the caroussel
        this.fetchCaroussel();
        setInterval(() => {
            this.fetchCaroussel();
        }, 1000 * 60 * 5);
        // Increment the current index every 10 seconds for the visible media
        setInterval(() => {
            this.activeIndex = Math.floor(Math.random() * this.medias.length);
        }, 10000);
    }
}
</script>
