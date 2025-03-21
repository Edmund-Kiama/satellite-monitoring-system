<script setup>
    import { defineProps, computed } from 'vue';

    const props = defineProps({
        data: Object,
        satellites: Array
    })

    const formatYear = (dateString) => {
    return new Date(dateString).getFullYear(); 
    }

    let satOption = computed(() => {
        if(!props.data || !props.satellites) {
            return null
        }

        let sat = props.satellites.find(sat => sat.id == props.data.sat_id)
        
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

                        <h3>{{ props.data.data_value}}</h3>

                        <ul>
                            <li>Data Type: <em> {{ props.data.data_type }} : {{ props.data.data_value }} </em></li>

                            <li>Source: {{ props.data.source }}</li>

                            <li>Satellite: {{  }}</li>

                            <li>Date Recorded: {{ formatYear(props.data.date_recorded) }}</li>
                        </ul>

                    </div>

                    <div class="block-detail">

                        <div>
                            <p>Value</p>
                            <p>{{ props.data.data_value }}</p>
                        </div> 

                        <div>
                            <p>Accuracy</p>
                            <p>{{ props.data.data_accuracy }}</p>
                        </div> 

                        <div>
                            <p>Units</p>
                            <p>{{ props.data.measurement_unit }}</p>
                        </div> 
                                 
                    </div>

                </div>

            </div>
            
</template>