<script setup>
    import { defineProps, defineEmits } from 'vue';
    
    const props = defineProps({
        data: Object,
        display: Object
    })

    const emit = defineEmits(['update:display'])
    const selectData = (sat) => {
        emit('update:display', sat)
    }

    const formatYear = (dateString) => {
    return new Date(dateString).getFullYear(); 
    };


</script>

<template>
    <div class="sat-side">
                <div class="search-name">
                    <input type="text" placeholder="Search Data Type">
                </div>

                <div class="filter">
                    <h3>Filter</h3>

                    <p class="sat-type">Data Type</p>
                    <select name="data-type" id="data-type">
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
                    <h3>Data ({{ data.length }})</h3>
                    <ul>
                        <li v-for="dat in props.data" :key="dat.id" @click="selectData(dat)">
                            <div>
                                <h4>{{ dat.name }}</h4>
                                <p>{{ dat.data_value }} | {{ formatYear(dat.recorded_date) }}</p>
                            </div>
                        </li>
                    </ul>
                </div>
                
            </div>
</template>