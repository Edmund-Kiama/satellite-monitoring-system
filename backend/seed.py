from mydb.models import db,Satellite, SatelliteData, Region
from datetime import date
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///monitoring.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db.init_app(app)

def add_seed():
    with app.app_context():
        db.create_all()
        # sat
        # db.session.query(Satellite).delete()
        # db.session.query(SatelliteData).delete()
        # db.session.query(Region).delete()
        # db.session.commit()
        
        landsat = Satellite(
            name = "Landsat-9",
            orbit_type = "LEO",
            status = "active",
            description = "NASA's Earth observation satellite",
            image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/LANDSAT-9.jpg/1024px-LANDSAT-9.jpg",
            country = "USA",
            altitude = "705 km",
            speed = "7.5 km/s",
            launch_date = date(2021,9,27),
            type = "Earth observation"
        )

        geos = Satellite(
            name = "GOES-16",
            orbit_type = "GEO",
            status = "active",
            description = "NOAA's weather satellite",
            image_url="https://www.nasa.gov/wp-content/uploads/2023/03/goesr_earth_reflection_2012.jpg?resize=1024,680",
            country = "USA",
            altitude = "35,786 km",
            speed = "3.07 km/s",
            launch_date = date(2016, 11, 19),
            type = "Weather satellite"
        )

        sentinel = Satellite(
            name = "Sentinel-2",
            orbit_type = "LEO",
            status = "active",
            description = "ESA's Earth observation satellite for land monitoring",
            image_url = "https://sentiwiki.copernicus.eu/__attachments/1671710/image-20230517-132224.png?inst-v=4ffdc811-3c3b-4ab5-969e-474a9a1b69a6",
            country = "European Union",
            altitude = "786 km",
            speed = "7.4 km/s",
            launch_date = date(2015, 6, 23),
            type = "Earth observation"
        )

        himawari = Satellite(
            name = "Himawari-8",
            orbit_type = "GEO",
            status = "active",
            description = "Japan's weather satellite for Asia-Pacific region",
            image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f2/Himawari89_2.jpg/1024px-Himawari89_2.jpg",
            country = "Japan",
            altitude = "35,786 km",
            speed = "3.07 km/s",
            launch_date = date(2014, 10, 7),
            type = "Weather satellite"
        )

        terra = Satellite(
            name = "Terra",
            orbit_type = "LEO",
            status = "active",
            description = "NASA's satellite for global climate and environmental research",
            image_url = "https://www.eoportal.org/ftp/satellite-missions/t/Terra_200722/Terra_Auto37.jpeg",
            country = "USA",
            altitude = "705 km",
            speed = "7.5 km/s",
            launch_date = date(1999, 12, 18),
            type = "Earth observation"
        )

        aqua = Satellite(
            name = "Aqua",
            orbit_type = "LEO",
            status = "active",
            description = "NASA's Earth observation satellite for studying water cycles",
            image_url = "https://earthdata.nasa.gov/s3fs-public/styles/hds_large/public/2022-05/AQUA.jpg?VersionId=Oob7cXtgOlFtFmCRIFe2XhnONGC.5inP&itok=kdsMI9DT",
            country = "USA",
            altitude = "705 km",
            speed = "7.5 km/s",
            launch_date = date(2002, 5, 4),
            type = "Earth observation"
        )

        cosmo_sky = Satellite(
            name = "COSMO-SkyMed",
            orbit_type = "LEO",
            status = "active",
            description = "Italian radar satellite for Earth observation and disaster monitoring",
            image_url = "https://www.eoportal.org/api/cms/documents/163813/3649508/COSMO_Auto32.jpeg",
            country = "Italy",
            altitude = "620 km",
            speed = "7.6 km/s",
            launch_date = date(2007, 6, 8),
            type = "Radar Earth observation"
        )

        insat_3d = Satellite(
            name = "INSAT-3D",
            orbit_type = "GEO",
            status = "active",
            description = "India's weather and environmental monitoring satellite",
            image_url = "https://sky-brokers.com/wp-content/uploads/2024/07/INSAT-3DS-in-orbit.jpeg",
            country = "India",
            altitude = "35,786 km",
            speed = "3.07 km/s",
            launch_date = date(2013, 7, 26),
            type = "Weather satellite"
        )
        # Inactive Satellites

        spacelab = Satellite(
            name = "Spacelab",
            orbit_type = "LEO",
            status = "inactive",
            description = "A reusable laboratory in space used by NASA and ESA for various research missions",
            image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Spacelab.jpg/800px-Spacelab.jpg",
            country = "USA/ESA",
            altitude = "300 km",
            speed = "7.6 km/s",
            launch_date = date(1983, 12, 28),
            type = "Space laboratory"
        )

        hubble = Satellite(
            name = "Hubble Space Telescope",
            orbit_type = "LEO",
            status = "inactive",
            description = "NASA's space telescope for observing distant galaxies and stars",
            image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Hubble_Space_Telescope_in_orbit.jpg/1024px-Hubble_Space_Telescope_in_orbit.jpg",
            country = "USA",
            altitude = "547 km",
            speed = "7.5 km/s",
            launch_date = date(1990, 4, 24),
            type = "Space telescope"
        )

        chandrayaan_1 = Satellite(
            name = "Chandrayaan-1",
            orbit_type = "Lunar",
            status = "inactive",
            description = "India's first lunar exploration satellite, part of the Chandrayaan program",
            image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Chandrayaan-1.jpg/800px-Chandrayaan-1.jpg",
            country = "India",
            altitude = "200 km (lunar orbit)",
            speed = "1.6 km/s",
            launch_date = date(2008, 10, 22),
            type = "Lunar exploration"
        )

        stardust = Satellite(
            name = "Stardust",
            orbit_type = "Solar orbit",
            status = "inactive",
            description = "NASA's mission to collect comet dust and return samples to Earth",
            image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Stardust-spacecraft.jpg/1024px-Stardust-spacecraft.jpg",
            country = "USA",
            altitude = "Varies (solar orbit)",
            speed = "13.5 km/s",
            launch_date = date(1999, 2, 7),
            type = "Cometary dust collection"
        )

        vanguard_1 = Satellite(
            name = "Vanguard 1",
            orbit_type = "LEO",
            status = "inactive",
            description = "The second satellite launched by the United States, used for scientific experiments",
            image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Vanguard_1_01.jpg/800px-Vanguard_1_01.jpg",
            country = "USA",
            altitude = "650 km",
            speed = "8 km/s",
            launch_date = date(1958, 3, 17),
            type = "Scientific satellite"
        )

        skylab = Satellite(
            name = "Skylab",
            orbit_type = "LEO",
            status = "inactive",
            description = "NASA's first space station used for medical, biological, and space physics research",
            image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/Skylab.jpg/800px-Skylab.jpg",
            country = "USA",
            altitude = "435 km",
            speed = "7.7 km/s",
            launch_date = date(1973, 5, 14),
            type = "Space station"
        )
        envisat = Satellite(
            name = "Envisat",
            orbit_type = "LEO",
            status = "inactive",
            description = "A European Space Agency satellite used for Earth observation, with a focus on environmental monitoring",
            image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c0/Envisat.jpg/800px-Envisat.jpg",
            country = "European Space Agency (ESA)",
            altitude = "800 km",
            speed = "7.5 km/s",
            launch_date = date(2002, 3, 1),
            type = "Earth observation"
        )

        seawifs = Satellite(
            name = "SeaWiFS",
            orbit_type = "LEO",
            status = "inactive",
            description = "NASA's satellite used for monitoring the Earth's oceans and collecting oceanographic data",
            image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/SeaWiFS.jpg/800px-SeaWiFS.jpg",
            country = "USA",
            altitude = "705 km",
            speed = "7.5 km/s",
            launch_date = date(1997, 7, 1),
            type = "Oceanographic satellite"
        )
 

        db.session.add_all([landsat, geos, sentinel, himawari, terra, aqua, cosmo_sky, insat_3d, spacelab, hubble, chandrayaan_1, stardust, vanguard_1, skylab, envisat, seawifs])
        db.session.commit()

        #region
        amazon = Region(
            sat_id = 1,  # landsat_id
            name = "Amazon Rainforest",
            latitude = -3.4653,
            longitude = -62.2159,
            area = "5.5 million km²",
            climate_type = "Tropical Rainforest",
            primary_focus = "Deforestation monitoring, biodiversity conservation"
        )

        sahara = Region(
            sat_id = 1,  # landsat_id
            name = "Sahara Desert",
            latitude = 23.4162,
            longitude = 25.6628,
            area = "9.2 million km²",
            climate_type = "Arid (Desert)",
            primary_focus = "Desertification, climate change impact monitoring"
        )

        east_coast = Region(
            sat_id = 2,  # geos_id
            name = "East Coast(US)",
            latitude = 35.2271,
            longitude = -80.8431,
            area = "1.5 million km²",
            climate_type = "Humid subtropical",
            primary_focus = "Weather forecasting, storm tracking"
        )

        mexico_gulf = Region(
            sat_id = 2,  # geos_id
            name = "Gulf of Mexico",
            latitude = 25.00,
            longitude = -90.00,
            area = "1.5 million km²",
            climate_type = "Tropical",
            primary_focus = "Hurricane tracking, coastal ecosystem monitoring"
        )

        great_barrier_reef = Region(
            sat_id = 3,  # sentinel_id
            name = "Great Barrier Reef",
            latitude = -18.2871,
            longitude = 147.6992,
            area = "344,400 km²",
            climate_type = "Tropical Marine",
            primary_focus = "Coral reef monitoring, ocean health tracking"
        )

        himalayas = Region(
            sat_id = 3,  # sentinel_id
            name = "Himalayas",
            latitude = 27.9881,
            longitude = 86.9250,
            area = "1.5 million km²",
            climate_type = "Alpine",
            primary_focus = "Glacier monitoring, environmental change research"
        )

        philippine_sea = Region(
            sat_id = 4,  # himawari_id
            name = "Philippine Sea",
            latitude = 15.0,
            longitude = 130.0,
            area = "5 million km²",
            climate_type = "Tropical",
            primary_focus = "Typhoon tracking, marine resource monitoring"
        )

        antarctica = Region(
            sat_id = 5,  # terra_id
            name = "Antarctica",
            latitude = -75.2500,
            longitude = -0.0714,
            area = "14 million km²",
            climate_type = "Polar (Cold desert)",
            primary_focus = "Climate change research, ice sheet monitoring"
        )

        greenland = Region(
            sat_id = 6,  # aqua_id
            name = "Greenland Ice Sheet",
            latitude = 71.7069,
            longitude = -42.6043,
            area = "1.7 million km²",
            climate_type = "Polar",
            primary_focus = "Glacier melt, sea level rise monitoring"
        )

        andes_mountains = Region(
            sat_id = 7,  # cosmo_sky_id
            name = "Andes Mountains",
            latitude = -32.6532,
            longitude = -70.0115,
            area = "7 million km²",
            climate_type = "Mountain climate",
            primary_focus = "Mountain ecosystem monitoring, disaster response"
        )

        indian_ocean = Region(
            sat_id = 8,  # insat_3d_id
            name = "Indian Ocean",
            latitude = -10.0,
            longitude = 80.0,
            area = "73.56 million km²",
            climate_type = "Tropical to subtropical",
            primary_focus = "Cyclone monitoring, maritime navigation support"
        )

        hurricane_zone = Region(
            sat_id = 8,  # insat_3d_id
            name = "Hurricane Formation Zone",
            latitude = 12.5,
            longitude = -60.0,
            area = "Varies annually",
            climate_type = "Tropical",
            primary_focus = "Hurricane and storm tracking"
        )

        db.session.add_all([amazon, sahara, east_coast, mexico_gulf, great_barrier_reef, 
                            himalayas, philippine_sea, antarctica, greenland, andes_mountains, 
                            indian_ocean, hurricane_zone
                           ])
        db.session.commit()

        #sat data
        surface_temp = SatelliteData(
            sat_id = 1,  # Landsat-9 ID
            data_type = "Surface Temperature",
            data_value = "32°C",
            date_recorded = date(2024, 12, 27),
            data_accuracy = "± 0.2°C",
            measurement_unit = "°C",
            source = "Thermal infrared sensor",
            satellite_orbit = "LEO"
        )

        vegetation_index = SatelliteData(
            sat_id = 1,  # Landsat-9 ID
            data_type = "NDVI (Vegetation Index)",
            data_value = "0.75",
            date_recorded = date(2025, 3, 9),
            data_accuracy = "± 0.05",
            measurement_unit = "NDVI",
            source = "Multispectral imaging",
            satellite_orbit = "LEO"
        )

        cloud_cover = SatelliteData(
            sat_id = 2,  # GOES-16 ID
            data_type = "Cloud Cover",
            data_value = "65%",
            date_recorded = date(2025, 2, 10),
            data_accuracy = "± 3%",
            measurement_unit = "%",
            source = "Imaging radiometers",
            satellite_orbit = "GEO"
        )

        wind_speed = SatelliteData(
            sat_id = 2,  # GOES-16 ID
            data_type = "Wind Speed",
            data_value = "120 km/h",
            date_recorded = date(2025, 3, 6),
            data_accuracy = "± 5 km/h",
            measurement_unit = "km/h",
            source = "Wind profiler radar",
            satellite_orbit = "GEO"
        )

        ocean_temp = SatelliteData(
            sat_id = 3,  # Sentinel-2 ID
            data_type = "Sea Surface Temperature",
            data_value = "28°C",
            date_recorded = date(2025, 1, 15),
            data_accuracy = "± 0.5°C",
            measurement_unit = "°C",
            source = "Thermal infrared sensor",
            satellite_orbit = "LEO"
        )

        air_quality = SatelliteData(
            sat_id = 3,  # Sentinel-2 ID
            data_type = "Air Quality Index",
            data_value = "AQI 42 (Good)",
            date_recorded = date(2025, 2, 5),
            data_accuracy = "± 2",
            measurement_unit = "AQI",
            source = "Airborne sensors",
            satellite_orbit = "LEO"
        )

        hurricane_intensity = SatelliteData(
            sat_id = 4,  # Himawari-8 ID
            data_type = "Hurricane Intensity",
            data_value = "Category 4",
            date_recorded = date(2025, 3, 8),
            data_accuracy = "± 0.1 category",
            measurement_unit = "Category",
            source = "Visible light and infrared imaging",
            satellite_orbit = "GEO"
        )

        ozone_levels = SatelliteData(
            sat_id = 5,  # Terra ID
            data_type = "Ozone Concentration",
            data_value = "290 DU",
            date_recorded = date(2025, 3, 10),
            data_accuracy = "± 10 DU",
            measurement_unit = "DU (Dobson Units)",
            source = "Ozone monitoring spectrometer",
            satellite_orbit = "LEO"
        )

        sea_level_rise = SatelliteData(
            sat_id = 6,  # Aqua ID
            data_type = "Sea Level Rise",
            data_value = "3.2 mm/year",
            date_recorded = date(2025, 1, 20),
            data_accuracy = "± 0.1 mm/year",
            measurement_unit = "mm/year",
            source = "Satellite altimetry",
            satellite_orbit = "LEO"
        )

        polar_ice_extent = SatelliteData(
            sat_id = 6,  # Aqua ID
            data_type = "Polar Ice Extent",
            data_value = "12.5 million km²",
            date_recorded = date(2025, 2, 18),
            data_accuracy = "± 0.5 million km²",
            measurement_unit = "million km²",
            source = "Radar altimetry",
            satellite_orbit = "LEO"
        )

        earthquake_detection = SatelliteData(
            sat_id = 7,  # COSMO-SkyMed ID
            data_type = "Ground Displacement",
            data_value = "5.3 cm shift",
            date_recorded = date(2025, 3, 5),
            data_accuracy = "± 0.1 cm",
            measurement_unit = "cm",
            source = "Synthetic aperture radar (SAR)",
            satellite_orbit = "LEO"
        )

        solar_radiation = SatelliteData(
            sat_id = 8,  # INSAT-3D ID
            data_type = "Solar Radiation",
            data_value = "1361 W/m²",
            date_recorded = date(2025, 2, 25),
            data_accuracy = "± 3 W/m²",
            measurement_unit = "W/m²",
            source = "Radiation sensor",
            satellite_orbit = "GEO"
        )

        precipitation_rate = SatelliteData(
            sat_id = 8,  # INSAT-3D ID
            data_type = "Precipitation Rate",
            data_value = "15 mm/hr",
            date_recorded = date(2025, 3, 12),
            data_accuracy = "± 0.5 mm/hr",
            measurement_unit = "mm/hr",
            source = "Passive microwave sensor",
            satellite_orbit = "GEO"
        )

        # Inactive Satellite Data

        inactive_satellite_data = SatelliteData(
            sat_id = 10,  # Example: Hubble Space Telescope (Inactive)
            data_type = "Cosmic Radiation",
            data_value = "2.5 mSv",
            date_recorded = date(2021, 4, 30),  # Last recording before inactivity
            data_accuracy = "± 0.2 mSv",
            measurement_unit = "mSv",
            source = "Radiation sensor (Hubble)",
            satellite_orbit = "LEO",
        )

        inactive_earth_observation = SatelliteData(
            sat_id = 15,  # Example: Envisat (Inactive)
            data_type = "Atmospheric Carbon Dioxide",
            data_value = "380 ppm",
            date_recorded = date(2012, 4, 8),  # Last recording before inactivity
            data_accuracy = "± 5 ppm",
            measurement_unit = "ppm",
            source = "Infrared spectrometer",
            satellite_orbit = "LEO",
        )

        inactive_ocean_monitoring = SatelliteData(
            sat_id = 16,  # Example: SeaWiFS (Inactive)
            data_type = "Ocean Chlorophyll Concentration",
            data_value = "0.12 mg/m³",
            date_recorded = date(2010, 6, 16),  # Last recording before inactivity
            data_accuracy = "± 0.01 mg/m³",
            measurement_unit = "mg/m³",
            source = "Ocean color sensor",
            satellite_orbit = "LEO",
        )


        db.session.add_all([surface_temp, vegetation_index, cloud_cover, wind_speed, ocean_temp, air_quality, hurricane_intensity,
                            ozone_levels, sea_level_rise, polar_ice_extent, earthquake_detection, solar_radiation, precipitation_rate,
                            inactive_satellite_data, inactive_earth_observation, inactive_ocean_monitoring
                            ])
        db.session.commit()

add_seed()


