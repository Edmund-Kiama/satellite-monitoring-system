<script setup>
    import { useRoute, useRouter } from 'vue-router';

    const router = useRouter()
    const route = useRoute()

    const navigate2Sat = () => {
        if (route.path === "/") {
            let element = document.getElementById("nav-to")
            element.scrollIntoView({
                behavior: 'smooth'
            })
        }
        else {
            router.push("/").then(() => {
                setTimeout(() => {
                    let element = document.getElementById("nav-to")
                    element.scrollIntoView({
                        behavior: 'smooth'
                    })
                }, 100)
            })            
        }
    }

    const navigate2SatData = () => {
        if (route.path === "/satellites-data") {
            let element = document.getElementById("nav-to")
            element.scrollIntoView({
                behavior: 'smooth'
            })
        }
        else {
            router.push("/satellites-data").then(() => {
                setTimeout(() => {
                    let element = document.getElementById("nav-to")
                    element.scrollIntoView({
                        behavior: 'smooth'
                    })
                }, 100)
            })            
        }
    }

    const navigate2SatRegion = () => {
        if (route.path === "/regions") {
            let element = document.getElementById("nav-to")
            element.scrollIntoView({
                behavior: 'smooth'
            })
        }
        else {
            router.push("/regions").then(() => {
                setTimeout(() => {
                    let element = document.getElementById("nav-to")
                    element.scrollIntoView({
                        behavior: 'smooth'
                    })
                }, 100)
            })            
        }
    }

    const selectedNavClass = (path) => {
        return route.path === path ? "selected" : ""
    }

</script>

<template>

    <div class="navbar">

        <img src="https://cdn-icons-png.flaticon.com/128/6186/6186680.png" alt="sat-logo">

        <nav>
            <ul>
                <li><a href="#landing-page">Home</a></li>

                <li><a :class="selectedNavClass('/')"  @click="navigate2Sat">Satellites</a></li>

                <li><a :class="selectedNavClass('/satellites-data')" @click="navigate2SatData">SatellitesData</a></li>
                
                <li><a :class="selectedNavClass('/regions')" @click="navigate2SatRegion">Regions</a></li>
            </ul>
        </nav>

    </div>

</template>