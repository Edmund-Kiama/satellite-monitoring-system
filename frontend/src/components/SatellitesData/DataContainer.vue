<script setup> 
    import DataMain from './DataMain.vue';
    import DataSide from './DataSide.vue';
    import { defineProps,ref } from 'vue';

    let display =ref(null)
    const props = defineProps({
        data: Array
    })

</script>

<template>
    <div class="satellite">
        <DataSide :data="data" :display="display" @update:display="display = $event"/>
        <DataMain v-if="display" :data="display"/>
        <DataMain v-else :data="data[0]"/>
        <div class="sat-main-empty"></div>
    </div>
</template>