<script setup>
    import { defineProps } from 'vue';

    const props = defineProps({
        data: Object
    })

    const formatYear = (dateString) => {
    return new Date(dateString).getFullYear(); 
    };
</script>

<template>
    <div class="sat-main">
                <!-- <div>
                    <img :src="props.satellites.image_url" alt="satellite-image">
                </div> -->
                
                <div class="main-detail-ui">
                    <div class="text-detail">
                        <h3>{{ props.data.data_value}}</h3>
                        <ul>
                            <li>type: {{ props.data.data_type }}</li>
                            <li>type: {{ props.data.data_type }}</li>
                            <li>type: {{ props.data.data_type }}</li>
                            <li>type: {{ props.data.data_type }}</li>
                            <li>type: {{ props.data.data_type }}</li>
                            <li>type: {{ props.data.data_type }}</li>
                            <li>type: {{ props.data.data_type }}</li>
                            <li>type: {{ props.data.data_type }}</li>
                            <!-- <li>orbit_type: {{ props.satellites.orbit_type }} </li>
                            <li>launch date: {{ formatYear(props.satellites.launch_date) }}</li> -->
                        </ul>
                    </div>
                    <div class="block-detail">
                        <!-- <div>
                            <p>Altitude</p>
                            <p>{{ props.satellites.altitude }}</p>
                        </div> 
                        <div>
                            <p>Speed</p>
                            <p>{{ props.satellites.speed }}</p>
                        </div>    
                        <div>
                            <p>Country</p>
                            <p>{{ props.satellites.country}}</p>
                        </div>  
                        <div>
                            <p>Status</p>
                            <p>{{ props.satellites.status }}</p>
                        </div>            -->
                    </div>
                </div>
            </div>
</template>