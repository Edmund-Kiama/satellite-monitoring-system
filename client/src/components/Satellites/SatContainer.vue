<script setup> 
    import SatMain from './SatMain.vue';
    import SatSide from './SatSide.vue';
    import { defineProps,ref } from 'vue';

    let display =ref(null)
    const props = defineProps({
        satellites: Array
    })

</script>

<template>

    <div class="satellite">

        <SatSide :satellites="satellites" :display="display" @update:display="display = $event"/>

        <SatMain v-if="display" :satellite="display"/>

        <SatMain v-else :satellite="satellites[0]"/>

        <div class="sat-main-empty"></div>

    </div>
    
</template>