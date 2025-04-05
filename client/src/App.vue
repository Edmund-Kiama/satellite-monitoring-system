<script setup>
   
    import Navbar from './components/Navbar.vue';
    import LandingPage from './components/LandingPage.vue';
    import {ref, onMounted} from 'vue';

    const URL = 'http://localhost:5555'
    const satelliteURL = '/satellites'
    const dataURL = '/satellites-data'
    const regionURL = '/regions'

    let sats = ref(null)
    let data = ref(null)
    let regions = ref(null)
    let error = ref(null)

    const fetchSats = async () => {
        try{
            let response = await fetch(satelliteURL)
            sats.value = await response.json()
            
        } catch (error) {
            error.value = "Failed to Fetch"
        }
    }
    const fetchSatData = async () => {
        try{
            let response = await fetch(dataURL)
            data.value = await response.json()
            
        } catch (error) {
            error.value = "Failed to Fetch"
        }
    }
    const fetchRegions = async () => {
        try{
            let response = await fetch(regionURL)
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