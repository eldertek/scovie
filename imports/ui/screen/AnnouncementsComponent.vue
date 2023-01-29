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
                { id: 0, type: "ABSENCE", text: "Le professeur de mathématiques est absent" },
                { id: 1, type: "ABSENCE", text: "Le professeur de français est absent" },
                { id: 2, type: "ABSENCE", text: "Le professeur de mathématiques est absent" },
                { id: 3, type: "ABSENCE", text: "Le professeur de physique est absent" },
                { id: 4, type: "ABSENCE", text: "Le professeur de emc est absent" },
                { id: 5, type: "ABSENCE", text: "Le professeur de philosophie est absent" },
                { id: 6, type: "ABSENCE", text: "Le professeur de histoire est absent" },
                { id: 7, type: "ABSENCE", text: "Le professeur de géographie est absent" },
                { id: 8, type: "ABSENCE", text: "Le professeur de humanité est absent" },
                { id: 9, type: "ABSENCE", text: "Le professeur de eps est absent" },
            ],
            currentIndex: 0
        }
    },
    mounted() {
        setInterval(() => {
            console.log(this.currentIndex);
            this.currentIndex = (this.currentIndex + 1) % this.announcements.length;
            console.log('next');
            console.log(this.currentIndex);
        }, 3000);
        window.addEventListener("resize", this.updateMaxVisible);
    },
    computed: {
        visibleAnnouncements() {
            console.log(this.announcements.slice(this.currentIndex, this.currentIndex + this.maxVisible));
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
        updateMaxVisible() {
            this.$forceUpdate();
        }
    }
}
</script>