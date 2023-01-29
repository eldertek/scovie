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
export default {
    name: "PlanningComponent",
    computed: {
        filteredRooms() {
            return this.rooms.filter(room => this.hasTeacher(room.name))
        }
    },
    methods: {
        hasTeacher(roomName) {
            return this.planning.some(plan => plan.room === roomName)
        }
    },
    data() {
        return {
            times: [
                { id: 1, name: "M1" },
                { id: 2, name: "M2" },
                { id: 3, name: "M3" },
                { id: 4, name: "M4" },
                { id: 5, name: "S1" },
                { id: 6, name: "S2" },
                { id: 7, name: "S3" },
                { id: 8, name: "S4" },
            ],
            rooms: [ 
                { id: 1, name: "A10" },
                { id: 2, name: "A20" },
                { id: 3, name: "A30" },
                { id: 4, name: "A40" },
                { id: 5, name: "A50" },
                { id: 6, name: "A60" },
                { id: 7, name: "A70" },
            ],
            planning: [
                { id: 1, time: 'M1', room: 'A20', teacher: 'Mr. Smith' },
                { id: 2, time: 'M2', room: 'A30', teacher: 'Mrs. Johnson' },
                { id: 3, time: 'S3', room: 'A50', teacher: 'Mr. Williams' },
                { id: 4, time: 'S4', room: 'A70', teacher: 'Mrs. Jones' },
            ]
        }
    }
}
</script>