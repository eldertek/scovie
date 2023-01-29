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
export default {
    name: "AnnouncementsComponent",
    data() {
        return {
            announcements: [
                { id: 1, type: "Absence", text: 'Le professeur de français est absent' },
                { id: 2, type: "Absence", text: 'Le professeur d\'anglais est absent' },
                { id: 3, type: "Absence", text: 'Le professeur de mathématiques est absent' },
                { id: 4, type: "Absence", text: 'Le professeur de physique est absent' },
                { id: 5, type: "Absence", text: 'Le professeur de chimie est absent' },
                { id: 6, type: "Absence", text: 'Le professeur d\'informatique est absent' },
                { id: 7, type: "Absence", text: 'Le professeur de SVT est absent' },
            ],
            currentIndex: 0
        }
    },
    mounted() {
        this.fetchAnnouncements();
        setInterval(() => {
            this.currentIndex = (this.currentIndex + 1) % this.announcements.length;
        }, 3000);
        window.addEventListener("resize", this.updateMaxVisible);
    },
    computed: {
        visibleAnnouncements() {
            return this.announcements.slice(this.currentIndex, this.currentIndex + this.maxVisible);
        },
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
    },
    methods: {
        fetchAnnouncements() {
            // Fetch announcements from an API or database
            // and store them in the announcements array
            // Example:
            // axios.get("/api/announcements").then(response => {
            //   this.announcements = response.data;
            // });
            // or
            // this.announcements = JSON.parse(localStorage.getItem("announcements"))
        },
        updateIndex() {
            requestAnimationFrame(() => {
                this.currentIndex = (this.currentIndex + 1) % this.announcements.length;
                this.updateIndex();
            });
        },
        updateMaxVisible() {
            this.$forceUpdate();
        }
    }
}
</script>