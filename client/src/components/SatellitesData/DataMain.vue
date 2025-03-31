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
    <div>
        <div class="sat-main" v-if="props.data">
            <div class="sat-img">
                <img :src="satOption" alt="satellite-image" v-if="satOption">
                <img src="https://i.pinimg.com/originals/c5/eb/05/c5eb05561c26dcd11228ed33cd3e707c.gif" alt="satellite-image" v-else>
            </div>
            
            <div class="main-detail-ui">

                <div class="text-detail">

                    <h3>Data Type: {{ props.data.data_type}}</h3>

                    <ul>

                        <li>Source: {{ props.data.source }}</li>

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

        <div class="sat-main" v-else>
            <img src="https://i.pinimg.com/originals/d8/75/32/d87532bf817b54ec2743c208ccfe5a4c.gif" alt="loading...">
        </div>
    </div>
            
</template>