<script setup>
    import { defineProps } from 'vue';

    const props = defineProps({
        satellite: Object
    })

    const formatYear = (dateString) => {
    return new Date(dateString).getFullYear(); 
    }
    
</script>

<template>
    <div>
        <div class="sat-main" v-if="props.satellite">

            <div>
                <img :src="props.satellite.image_url" alt="satellite-image">
            </div>

            
            <div class="main-detail-ui">

                <div class="text-detail">

                    <h3>{{ props.satellite.name}}</h3>

                    <ul>
                        <li>Type: {{ props.satellite.type }}</li>

                        <li>Orbit Type: {{ props.satellite.orbit_type }} </li>

                        <li>Launch Year: {{ formatYear(props.satellite.launch_date) }}</li>

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
        <div class="sat-main" v-else>
            <img src="https://i.pinimg.com/originals/d8/75/32/d87532bf817b54ec2743c208ccfe5a4c.gif" alt="loading...">
        </div>
    </div>
</template>