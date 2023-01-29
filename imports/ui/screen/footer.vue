<template>
    <nav :class="{'fixed-bottom': isDesktop, 'bottom': !isDesktop}" class="navbar bg-white" style="--bs-bg-opacity: .20;">
        <div class="container-fluid">
            <span class="navbar-brand mb-0 h1 fs-6 text-start text-light">
                Développé par André Théo LAURET
            </span>
        </div>
    </nav>
</template>
<script>
export default {
    name: "FooterComponent",
    data() {
        return {
            isDesktop: window.innerWidth > 767
        }
    },
    mounted() {
        window.addEventListener('resize', this.handleResize)
    },
    methods: {
        handleResize() {
            this.isDesktop = window.innerWidth > 767
        }
    }
}
</script>