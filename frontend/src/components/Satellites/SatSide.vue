<script setup>
    import { defineProps, defineEmits } from 'vue';
    
    const props = defineProps({
        satellites: Object,
        display: Object
    })

    const emit = defineEmits(['update:display'])
    const selectSatellite = (sat) => {
        emit('update:display', sat)
    }

    const formatYear = (dateString) => {
    return new Date(dateString).getFullYear(); 
    };


</script>

<template>
    <div class="sat-side">
                <div class="search-name">
                    <input type="text" placeholder="Search satellites">
                </div>

                <div class="filter">
                    <h3>Filter</h3>

                    <p class="sat-type">Satellite Type</p>
                    <select name="satellite-type" id="sat-type">
                        <option value="">Choose a type</option>
                    </select>
                

                    <p class="altitude">Altitude Range</p>
                    <div class="altitude-io">
                        <input type="range" id="altitude" name="altitude" min="50000" max="500000" step="1000" value="100000" oninput="altValue.value = this.value">
                        <em><output id="altValue">100000</output> km</em>
                    </div>
                    

                    <p class="status">Status</p>
                    <div class="checkbox">
                        <label for="active" class="active">
                            <input type="checkbox" id="active" value="active" name="active" checked>
                            Active
                        </label>
                        <label for="inactive" class="inactive">
                            <input type="checkbox" id="inactive" value="inactive" name="inactive">
                            Inactive
                        </label>       
                    </div>             
                </div>   
                
                <div class="sat-results">
                    <h3>Satellites ({{ satellites.length }})</h3>
                    <ul>
                        <li v-for="sat in props.satellites" :key="sat.id" @click="selectSatellite(sat)">
                            <div>
                                <h4>{{ sat.name }}</h4>
                                <p>{{ sat.country }} | {{ formatYear(sat.launch_date) }}</p>
                            </div>
                        </li>
                    </ul>
                </div>
                
            </div>
</template>