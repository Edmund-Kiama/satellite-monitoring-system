<script setup>
    import { ref, computed, defineProps, defineEmits } from 'vue';
    
    let search = ref("")
    let selectedSource = ref("")
    let selectedSat = ref("")
    let selectedOrbit = ref("")


    const props = defineProps({
        data: Array,
        satellites: Array,
        display: Object
    })

    const emit = defineEmits(['update:display'])
    const selectData = (dat) => {
        emit('update:display', dat)
    }

    const handleSearch = (event) => {
        search.value = event.target.value
    }

    let searchList = computed(() => {
        if (!props.data){
            return []
        } else {
            let searchedList = props.data.filter(data => {
                let searched = search.value.toLowerCase().trim()
                let selectSource = selectedSource.value.toLowerCase().trim() 
                let selectSat = selectedSat.value
                let selectOrbit = selectedOrbit.value.toLowerCase().trim()

                let matchSearch
                let matchSource
                let matchSat
                let matchOrbit

                if (searched === ""){
                    matchSearch = true
                } else {
                    matchSearch = data.data_type.toLowerCase().includes(searched)
                }


                if (selectSource === "") {
                    matchSource = true
                } else {
                    matchSource = data.source.toLowerCase().includes(selectSource)
                }


                if (isNaN(selectSat) ) {
                    matchSat = true 
                } else {
                    matchSat = String(data.sat_id).includes(selectSat)
                }


                if (selectOrbit === "") {
                    matchOrbit = true
                } else {
                    matchOrbit = data.satellite_orbit.toLowerCase().includes(selectOrbit)
                }

                
                return matchSearch && matchSource && matchSat && matchOrbit
            })

            return searchedList
        }
    })

    let sourceOption = computed(() => {
        let dataSource = []

        props.data.forEach(data => {
            let sourceExist = dataSource.includes(data.source)
            if (!sourceExist) {
                dataSource.push(data.source)
            }
        })
        return dataSource
    })

    let satOption = computed(() => {
        let dataSatId = []

        props.data.forEach(data => {
            let satExist = dataSatId.includes(data.sat_id)
            if (!satExist) {
                dataSatId.push(data.sat_id)
            }
        })

        let satName = []

        dataSatId.forEach(satId => {
            let sat = props.satellites.find(sat => sat.id == satId)
            if (sat) {
                satName.push(sat)
            }
        })

        return satName
    })

    let orbitOption = computed(() => {
        let orbits = []

        props.data.forEach(data => {
            let orbitExist = orbits.includes(data.satellite_orbit)
            if (!orbitExist) {
                orbits.push(data.satellite_orbit)
            }
        })

        return orbits
    })
 
    const handleReset = computed(() => {
        search.value = ""
        selectedSource.value = ""
        selectedSat.value = ""
        selectedOrbit.value = ""
    }) 


</script>

<template>

    <div class="sat-side">

                <div class="search-name">
                    <input type="text" placeholder="Search Data Type" v-model="search" @input="handleSearch">
                </div>

                <div class="filter">

                    <h3>Filter</h3>

                    <p class="sat-type">Data Source</p>

                    <select name="data-type" id="sat-type" v-model="selectedSource">
                        <option value="">Choose a source</option>
                        <option v-for="source in sourceOption" :key="source" :value="source">{{ source }}</option>
                    </select>


                    <p class="sat-type">Satellite Used</p>

                    <select name="sat-type" id="sat-type" v-model="selectedSat">
                        <option value="">Choose a satellite</option>
                        <option v-for="sat in satOption" :key="sat.id" :value="sat.id">{{ sat.name }}</option>
                    </select>
                    

                    <p class="status">Choose in terms of Orbit</p>

                    <div class="checkbox">

                        <label for="none" class="none">
                            <input type="radio" id="none" value="" v-model="selectedOrbit">
                        </label>  

                        <label for="active" class="active" v-for="orbit in orbitOption" :key="orbit" >
                            <input type="radio" id="active" :value="orbit" v-model="selectedOrbit" >
                            {{ orbit }}
                        </label>     

                    </div>   
                    
                    <div class="reset">
                        <button @click="handleReset">Reset</button>
                    </div>

                </div>   
                
                <div class="sat-results">

                    <h3>Data ({{ searchList.length }})</h3>

                    <ul v-if="searchList.length > 0">
                        
                        <li v-for="dat in searchList" :key="dat.id" @click="selectData(dat)" class="res">
                            
                            <div>
                                <h4>{{ dat.data_type }}</h4>
                                <p>{{ dat.data_value }} | {{ dat.data_accuracy }}</p>
                            </div>

                        </li>

                    </ul>

                    <p v-else>No Data Found</p>

                </div>
                
            </div>

</template>