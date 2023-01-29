<template>
    <div>
        <nav class="navbar bg-white" style="--bs-bg-opacity: .20;">
            <div class="container-fluid justify-content-center">
                <span class="navbar-brand text-light" style="font-size: 3vh;">
                    <strong>Organisation des salles de TP</strong>
                </span>
            </div>
        </nav>
        <table class="table table-bordered border-white table-dark table-striped" style="font-size: 2vh;">
            <thead>
                <tr>
                    <th></th>
                    <th v-for="room in filteredRooms" :key="room.id">{{ room.name }}</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="time in times" :key="time.id">
                    <td>{{ time.name }}</td>
                    <td v-for="room in filteredRooms" :key="room.id">
                        <template v-for="plan in planning" :key="plan.id">
                            <template v-if="plan.time === time.name && plan.room === room.name">
                                {{ plan.teacher }}
                            </template>
                        </template>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>
<script>
// Import axios for HTTP requests
import axios from 'axios'
// Export the component
export default {
    // The component's name
    name: "PlanningComponent",
    // The component's data
    data() {
        // Return the data
        return {
            // The times
            times: [],
            // The rooms
            rooms: [],
            // The planning
            planning: []
        }
    },
    // The component's computed properties
    computed: {
        // Filter the rooms
        filteredRooms() {
            return this.rooms.filter(room => this.hasTeacher(room.name))
        }
    },
    // The component's mounted hook
    mounted() {
        // Fetch all
        this.fetchTimes();
        this.fetchRooms();
        this.fetchPlanning();
        // Fetch all every 5 minutes
        setInterval(() => {
            this.fetchTimes();
            this.fetchRooms();
            this.fetchPlanning();
        }, 1000 * 60 * 5);
    },
    // The component's methods
    methods: {
        // Fetch the times
        fetchTimes() {
            // Get the configuration
            axios.get('http://localhost:3000/api/times')
                .then(response => {
                    this.times = response.data;
                })
                .catch(error => {
                    console.log(error);
                })
        },
        // Fetch the rooms
        fetchRooms() {
            // Get the configuration
            axios.get('http://localhost:3000/api/rooms')
                .then(response => {
                    this.rooms = response.data;
                })
                .catch(error => {
                    console.log(error);
                })
        },
        // Fetch the planning
        fetchPlanning() {
            // Get the configuration
            axios.get('http://localhost:3000/api/planning')
                .then(response => {
                    this.planning = response.data;
                })
                .catch(error => {
                    console.log(error);
                })
        },
        // Check if a room has a teacher
        hasTeacher(roomName) {
            return this.planning.some(plan => plan.room === roomName)
        }
    },
}
</script>