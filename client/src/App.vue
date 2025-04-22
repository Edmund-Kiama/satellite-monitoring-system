<script setup>
   
    import Navbar from './components/Navbar.vue';
    import LandingPage from './components/LandingPage.vue';
    import {ref, onMounted} from 'vue';

    const URL = 'https://satellite-monitoring-system.onrender.com'
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
        <div class="load" v-else>
            <img class="loading-gif" src="https://i.pinimg.com/originals/b8/71/76/b8717641f46cdfdced2c86e984f07c11.gif" alt="loading" >
        </div>
    </div>

</template>