<script setup>
    import { ref, computed, defineProps, defineEmits } from 'vue';
    
    let search = ref("")
    let selected = ref("")
    let selectedCountry = ref("")
    let selectedStatus = ref("")
    let selectedOrbit = ref("")

    const props = defineProps({
        satellites: Array,
        display: Object
    })

    const emit = defineEmits(['update:display'])
    const selectSatellite = (sat) => {
        emit('update:display', sat)
    }

    const formatYear = (dateString) => new Date(dateString).getFullYear(); 

    const handleSearch = (event) => {
        search.value = event.target.value
    }
    const handleSelect = (event) => {
        selected.value = event.target.value
    }

    let searchList = computed(() => {
        if (!props.satellites) {
            return []

        } else {
            let searchedList = props.satellites.filter(satellite => {
                let searched = search.value.toLowerCase().trim()
                let selectedType = selected.value.toLowerCase().trim()
                let selectedStat = selectedStatus.value.toLowerCase().trim()
                let selectCountry = selectedCountry.value.toLowerCase().trim()
                let selectOrbit = selectedOrbit.value.toLowerCase().trim()

                let matchName
                let matchType
                let matchStatus
                let matchCountry
                let matchOrbit

                if (searched === "") {
                    matchName = true
                } else {
                    matchName = satellite.name.toLowerCase().includes(searched)
                }


                if (selectedType === "") {
                    matchType = true
                } else {
                    matchType = satellite.type.toLowerCase().includes(selectedType)
                }


                if (selectedStatus.value === "") {
                    matchStatus = true
                } else {
                    matchStatus = satellite.status.toLowerCase() === selectedStat
                }


                if (selectCountry === "") {
                    matchCountry = true
                } else {
                    matchCountry = satellite.country.toLowerCase().includes(selectCountry)
                }


                if (selectedOrbit.value === "") {
                    matchOrbit = true
                } else {
                    matchOrbit = satellite.orbit_type.toLowerCase() === selectOrbit
                }


                return matchName && matchType && matchStatus && matchCountry && matchOrbit
            })

            return searchedList
        }
    })

    // idea: create an array that contains sat.type and it occurs once only
    let selectOption = computed(() => {
        let satType = []

        props.satellites.forEach(satellite => {
            let typeExist = satType.includes(satellite.type)
            if (!typeExist) {
                satType.push(satellite.type)
            }
        })
        return satType
    })

    let countryOption = computed(() => {
        let satCountry = []

        props.satellites.forEach(sat=> {
            let countryExist = satCountry.includes(sat.country)
            if (!countryExist) {
                satCountry.push(sat.country)
            }
        })
        return satCountry
    })

    let statusOption = computed(() => {
        let satStatus = []

        props.satellites.forEach(sat=> {
            let statusExist = satStatus.includes(sat.status)
            if (!statusExist) {
                satStatus.push(sat.status)
            }
        })
        return satStatus
    })

    let orbitOption = computed(() => {
        let satOrbit = []

        props.satellites.forEach(sat=> {
            let orbitExist = satOrbit.includes(sat.orbit_type)
            if (!orbitExist) {
                satOrbit.push(sat.orbit_type)
            }
        })
        return satOrbit
    })

    const handleReset = computed(() => {
        search.value = ""
        selected.value = ""
        selectedCountry.value = ""
        selectedStatus.value = ""
        selectedOrbit.value = ""
    }) 

</script>

<template>
    <div class="sat-side">

                <div class="search-name">

                    <input 
                        type="text" 
                        placeholder="Search satellites"
                        v-model="search"
                        @input="handleSearch"
                    >

                </div>

                <div class="filter"> 

                    <h3>Filter</h3>

                    <p class="sat-type">Satellite Type</p>

                    <select name="satellite-type" id="sat-type" v-model="selected">
                        <option value="">Choose a type</option>
                        <option v-for="type in selectOption" :key="type" :value="type">{{ type }}</option>
                    </select>


                    <p class="sat-type">Satellite Country</p>
                    
                    <select name="satellite-type" id="sat-type" v-model="selectedCountry">
                        <option value="">Choose a country</option>
                        <option v-for="country in countryOption" :key="country" :value="country">{{ country }}</option>
                    </select>
                    

                    <p class="status">Status</p>

                    <div class="checkbox">

                        <label for="none" class="none">
                            <input type="radio" id="none" value="" v-model="selectedStatus">
                        </label>    

                        <label for="active" class="active" v-for="stat in statusOption" :key="stat" >
                            <input type="radio" :id="stat" :value="stat" v-model="selectedStatus">
                            {{ stat }}
                        </label>

                    </div>    
                    

                    <p class="status">Orbit Type</p>

                    <div class="checkbox">
                        
                        <label for="none" class="none">
                            <input type="radio" id="none" value="" v-model="selectedOrbit">
                        </label>    

                        <label for="active" class="active"  v-for="orbit in orbitOption" :key="orbit" >
                            <input type="radio" :id="orbit" :value="orbit" v-model="selectedOrbit">
                            {{ orbit }}
                        </label>

                    </div> 

                    <div class="reset"> 

                        <button @click="handleReset">Reset</button>

                    </div>
                </div>   
                
                <div class="sat-results">

                    <h3>Satellites ({{  searchList.length }})</h3>

                    <ul v-if="searchList.length > 0">

                        <li v-for="sat in searchList" :key="sat.id" @click="selectSatellite(sat)" class="res">

                            <div>
                                <h4>{{ sat.name }}</h4>
                                <p>{{ sat.country }} | {{ formatYear(sat.launch_date) }}</p>
                            </div>

                        </li>
                        
                    </ul>

                    <ul v-else>

                        <li>No Satellites Found</li>

                    </ul>

                </div>

            </div>

</template>