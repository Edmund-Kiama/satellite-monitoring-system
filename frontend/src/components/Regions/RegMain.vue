<script setup>
    import { defineProps, computed } from 'vue';

    const props = defineProps({
        region: Object,
        satellites: Array
    })

    let satOption = computed(() => {
        if(!props.region || !props.satellites) {
            return null
        }

        let sat = props.satellites.find(sat => sat.id == props.region.sat_id)
        
        return sat.image_url
    })

</script>

<template>
    <div class="sat-main">
                <div>
                    <img :src="satOption" alt="satellite-image">
                </div>
                
                <div class="main-detail-ui"> 

                    <div class="text-detail">

                        <h3>{{ props.region.name}}</h3>

                        <ul>
                            <li>latitude: {{ props.region.latitude }}</li>

                            <li>longitude: {{ props.region.longitude }} </li>

                            <li>primary focus: {{ props.region.primary_focus }}</li>
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