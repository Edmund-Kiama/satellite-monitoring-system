import { createRouter, createWebHistory} from 'vue-router'
import SatContainer from './components/Satellites/SatContainer.vue'
import DataContainer from './components/SatellitesData/DataContainer.vue'
import RegContainer from './components/Regions/RegContainer.vue';

const routes = [
    {path: '/', component: SatContainer},
    {path: '/satellites-data', component: DataContainer},
    {path: '/regions', component: RegContainer}
]

const router = createRouter({
    history: createWebHistory(),
    routes,
    scrollBehavior(to) {
        if (to.hash) {
          return {
            el: to.hash, 
            behavior: 'smooth' 
          };
        }
    }
});

export default router

