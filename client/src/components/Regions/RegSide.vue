<script setup>
    import { computed, defineProps, defineEmits, ref } from 'vue';
    
    let search = ref("")
    let selectClimate = ref("")
    let selectSat = ref("")

    const props = defineProps({
        regions: Array,
        satellites: Array,
        display: Object
    })

    const emit = defineEmits(['update:display'])
    const selectRegion = (sat) => {
        emit('update:display', sat)
    }

    const handleSearch = (event) => {
        search.value = event.target.value
    }

    let searchList = computed(() => {
        if (!props.regions) {
            return []
        } else {
            let searchedList = props.regions.filter(reg => {
                let searched = search.value.toLowerCase().trim()
                let selectedClimate = selectClimate.value.toLowerCase().trim()
                let selectedSat = selectSat.value

                let matchSearch
                let matchClimate
                let matchSat

                if (searched === "") {
                    matchSearch = true
                } else {
                    matchSearch = reg.name.toLowerCase().includes(searched)
                }


                if (selectedClimate === "") {
                    matchClimate = true 
                } else {
                    matchClimate = reg.climate_type.toLowerCase().includes(selectedClimate)
                }


                if (isNaN(selectedSat) ) {
                    matchSat = true 
                } else {
                    matchSat = String(reg.sat_id).includes(selectedSat)
                }


                return matchSearch && matchClimate && matchSat
            })

            return searchedList
        }
    })

    let climateOption = computed(() => {
        let climate = []

        props.regions.forEach(reg => {
            let climateExist = climate.includes(reg.climate_type)
            if (!climateExist) {
                climate.push(reg.climate_type)
            }
        });
        return climate
    })

    let satOption = computed(() => {
        let regSatId = []

        props.regions.forEach(reg => {
            let satExist = regSatId.includes(reg.sat_id)
            if (!satExist) {
                regSatId.push(reg.sat_id)
            }
        })

        let satName = []

        regSatId.forEach(satId => {
            let sat = props.satellites.find(sat => sat.id == satId)
            if (sat) {
                satName.push(sat)
            }
        })

        return satName
    })

    const handleReset = computed(() => {
        search.value = ""
        selectClimate.value = ""
        selectSat.value = ""
    }) 

</script>

<template>
    <div class="sat-side">
        
                <div class="search-name">
                    <input type="text" placeholder="Search regions" :value="search" @input="handleSearch">
                </div>

                <div class="filter">

                    <h3>Filter</h3>

                    <p class="sat-type">Climate Type</p>

                    <select name="satellite-type" id="sat-type" v-model="selectClimate">
                        <option value="">Choose a climate</option>
                        <option v-for="climate in climateOption" :key="climate" :value="climate">{{ climate }}</option>
                    </select>

                    <p class="sat-type">Satellite Used</p>

                    <select name="sat-type" id="sat-type" v-model="selectSat">
                        <option value="">Choose a satellite</option>
                        <option v-for="sat in satOption" :key="sat.id" :value="sat.id">{{ sat.name }}</option>
                    </select>  
                    
                    <div class="reset">
                        <button @click="handleReset">Reset</button>
                    </div>

                </div>   
                
                <div class="sat-results">

                    <h3>Regions ({{ searchList.length }})</h3>

                    <ul v-if="searchList.length > 0">
                        <li v-for="reg in searchList" :key="reg.id" @click="selectRegion(reg)" class="res">

                            <div>
                                <h4>{{ reg.name }}</h4>

                                <p>{{ reg.climate_type }} | {{ reg.area }}</p>
                            </div>

                        </li>
                    </ul>

                    <p v-else >No Region Found</p>

                </div>
                
            </div>
</template>