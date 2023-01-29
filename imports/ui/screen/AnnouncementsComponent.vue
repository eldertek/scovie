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
            announcements: [],
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
            axios.get("/api/announcements").then(response => {
                this.announcements = response.data;
            });
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