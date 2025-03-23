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
    <div>
    <div class="sat-main" v-if="props.region">
        <div>
            <img :src="satOption" alt="satellite-image">
        </div>
        
        <div class="main-detail-ui"> 

            <div class="text-detail">

                <h3>{{ props.region.name}}</h3>

                <ul>
                    <li>Climate: {{ props.region.climate_type }}</li>

                    <li>Area: {{ props.region.area }} </li>

                    <li>primary focus: {{ props.region.primary_focus }}</li>
                </ul>

            </div>

            <div class="block-detail">
                <div>
                    <p>Latitude</p>
                    <p>{{ props.region.latitude }}</p>
                </div> 

                <div>
                    <p>Longitude</p>
                    <p>{{ props.region.longitude }}</p>
                </div>    
                    
            </div>
        </div>
    </div>
    <div class="sat-main" v-else>
            <img src="https://i.pinimg.com/originals/f4/ed/7a/f4ed7a58996957266401435585604881.gif" alt="loading...">
        </div>
    </div>
</template>