<script setup> 
    import RegSide from './RegSide.vue';
    import RegMain from './RegMain.vue';
    import { defineProps,ref } from 'vue';

    let display =ref(null)

    const props = defineProps({
        regions: Array,
        satellites: Array
    })

</script>

<template>

    <div class="satellite">

        <RegSide :regions="regions" :display="display" @update:display="display = $event" :satellites="satellites" />

        <RegMain v-if="display" :region="display" :satellites="satellites"/>

        <RegMain v-else :region="regions[0]"/>

        <div class="sat-main-empty"></div>

    </div>

</template>