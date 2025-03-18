<script setup>

</script>

<template>
    <div>
        <div class="navbar">
            <img src="../public/assests/satellite.png" alt="sat-logo">
            <nav>
                <ul>
                    <li><a href="#landing-page">Home</a></li>
                    <li><a href="#landing-page">Satellites</a></li>
                    <li><a href="#landing-page">Satellites Data</a></li>
                    <li><a href="#landing-page">Regions</a></li>
                </ul>
            </nav>
        </div>

        <div class="landing-page" id="landing-page">
            <h1>Real-Time Satellite Monitoring for a Smarter Future</h1>
            <h4>
                Monitor satellite data in real-time, analyze regions of interest, and gain insights with an intuitive dashboard. 
                Stay ahead with precise tracking and analytics.
            </h4>
        </div>

        <div class="satellite">
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
                    <ul>
                        <h3>Satellites(2)</h3>
                        <li>
                            <div>
                                <h4>Satellite Name</h4>
                                <p>Country | year</p>
                            </div>
                        </li>
                        <li>
                            <div>
                                <h4>Satellite Name 2</h4>
                                <p>Country2 | year 2</p>
                            </div>
                        </li>
                    </ul>
                </div>
                
            </div>

            <div class="sat-main"></div>
        </div>
    </div>

</template>