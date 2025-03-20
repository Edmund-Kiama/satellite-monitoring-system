<script setup>
//  landsat = Satellite(
//             name = "Landsat-9",
//             orbit_type = "LEO",
//             status = "active",
//             description = "NASA's Earth observation satellite",
//             image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/LANDSAT-9.jpg/1024px-LANDSAT-9.jpg",
//             country = "USA",
//             altitude = "705 km",
//             speed = "7.5 km/s",
//             launch_date = date(2021,9,27),
//             type = "Earth observation"
//         )
   
    import Navbar from './components/Navbar.vue';
    import LandingPage from './components/LandingPage.vue';
    import SatContainer from './components/Satellites/SatContainer.vue';
    import {ref, onMounted} from 'vue';

    const URL = 'http://127.0.0.1:5000'
    const satelliteURL = '/satellites'
    const dataURL = '/satellites-data'
    const regionURL = '/regions'

    let sats = ref(null)
    let data = ref(null)
    let regions = ref(null)
    let error = ref(null)

    const fetchSats = async () => {
        try{
            let response = await fetch(URL+satelliteURL)
            sats.value = await response.json()
            
        } catch (error) {
            error.value = "Failed to Fetch"
        }
    }
    const fetchSatData = async () => {
        try{
            let response = await fetch(URL+dataURL)
            data.value = await response.json()
            
        } catch (error) {
            error.value = "Failed to Fetch"
        }
    }
    const fetchRegions = async () => {
        try{
            let response = await fetch(URL+regionURL)
            regions.value = await response.json()
            
        } catch (error) {
            error.value = "Failed to Fetch"
        }
    }
    onMounted(() => {
        fetchSats();
        fetchSatData();
        fetchRegions();
    });
    
</script>

<template>
    <div>
        <Navbar />
        <LandingPage />       
        <div v-if="sats && data && regions">
            <router-view :satellites="sats" :data="data" :regions="regions" />
        </div>        
        <p v-else>Loading...</p>
    </div>

</template>