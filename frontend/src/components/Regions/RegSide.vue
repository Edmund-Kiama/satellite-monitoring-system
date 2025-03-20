<script setup>
    import { defineProps, defineEmits } from 'vue';
    
    const props = defineProps({
        regions: Object,
        display: Object
    })

    const emit = defineEmits(['update:display'])
    const selectRegion = (sat) => {
        emit('update:display', sat)
    }
</script>

<template>
    <div class="sat-side">
                <div class="search-name">
                    <input type="text" placeholder="Search satellites">
                </div>

                <div class="filter">
                    <h3>Filter</h3>

                    <p class="sat-type">Region</p>
                    <select name="satellite-type" id="sat-type">
                        <option value="">Choose a region</option>
                    </select>
                

                    <!-- <p class="altitude">Altitude Range</p>
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
                    </div>              -->
                </div>   
                
                <div class="sat-results">
                    <h3>Regions ({{ regions.length }})</h3>
                    <ul>
                        <li v-for="reg in props.regions" :key="reg.id" @click="selectRegion(reg)">
                            <div>
                                <h4>{{ reg.name }}</h4>
                                <p>{{ reg.climate_type }} | {{ reg.area }}</p>
                            </div>
                        </li>
                    </ul>
                </div>
                
            </div>
</template>