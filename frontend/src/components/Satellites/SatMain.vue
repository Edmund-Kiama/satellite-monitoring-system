<script setup>
    import { defineProps } from 'vue';

    const props = defineProps({
        satellite: Object
    })

    const formatYear = (dateString) => {
    return new Date(dateString).getFullYear(); 
    };
</script>

<template>
    <div class="sat-main">
                <div>
                    <img :src="props.satellite.image_url" alt="satellite-image">
                </div>
                
                <div class="main-detail-ui">
                    <div class="text-detail">
                        <h3>{{ props.satellite.name}}</h3>
                        <ul>
                            <li>type: {{ props.satellite.type }}</li>
                            <li>orbit_type: {{ props.satellite.orbit_type }} </li>
                            <li>launch date: {{ formatYear(props.satellite.launch_date) }}</li>
                        </ul>
                    </div>
                    <div class="block-detail">
                        <div>
                            <p>Altitude</p>
                            <p>{{ props.satellite.altitude }}</p>
                        </div> 
                        <div>
                            <p>Speed</p>
                            <p>{{ props.satellite.speed }}</p>
                        </div>    
                        <div>
                            <p>Country</p>
                            <p>{{ props.satellite.country}}</p>
                        </div>  
                        <div>
                            <p>Status</p>
                            <p>{{ props.satellite.status }}</p>
                        </div>           
                    </div>
                </div>
            </div>
</template>