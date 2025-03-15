from mydb.models import db,Satellite, SatelliteData, Region
from sqlalchemy import select
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
        landsat = Satellite(
            name = "Landsat-9",
            orbit_type = "LEO",
            status = "active",
            description = "NASA's Earth observation satellite"
        )
        landsat_id = db.session.execute(select(Satellite.id).where(Satellite.name == "Landsat-9")).scalar()

        geos = Satellite(
            name = "GOES-16",
            orbit_type = "GEO",
            status = "active",
            description = "NOAA's weather satellite"
        )
        geos_id = db.session.execute(select(Satellite.id).where(Satellite.name == "GEOS-16")).scalar()

        sentinel = Satellite(
            name = "Sentinel-2",
            orbit_type = "LEO",
            status = "active",
            description = "ESA's Earth observation satellite for land monitoring"
        )
        sentinel_id = db.session.execute(select(Satellite.id).where(Satellite.name == "Sentinel-2")).scalar()

        himawari = Satellite(
            name = "Himawari-8",
            orbit_type = "GEO",
            status = "active",
            description = "Japan's weather satellite for Asia-Pacific region"
        )
        himawari_id = db.session.execute(select(Satellite.id).where(Satellite.name == "Himawari-8")).scalar()

        terra = Satellite(
            name = "Terra",
            orbit_type = "LEO",
            status = "active",
            description = "NASA's satellite for global climate and environmental research"
        )
        terra_id = db.session.execute(select(Satellite.id).where(Satellite.name == "Terra")).scalar()

        aqua = Satellite(
            name = "Aqua",
            orbit_type = "LEO",
            status = "active",
            description = "NASA's Earth observation satellite for studying water cycles"
        )
        aqua_id = db.session.execute(select(Satellite.id).where(Satellite.name == "Aqua")).scalar()

        cosmo_sky = Satellite(
            name = "COSMO-SkyMed",
            orbit_type = "LEO",
            status = "active",
            description = "Italian radar satellite for Earth observation and disaster monitoring"
        )
        cosmo_sky_id = db.session.execute(select(Satellite.id).where(Satellite.name == "COSMOS-SkyMed")).scalar()

        insat_3d = Satellite(
            name = "INSAT-3D",
            orbit_type = "GEO",
            status = "active",
            description = "India's weather and environmental monitoring satellite"
        )
        insat_3d_id = db.session.execute(select(Satellite.id).where(Satellite.name == "INSAT-3D")).scalar()    

        db.session.add_all([landsat, geos, sentinel, himawari, terra, aqua, cosmo_sky, insat_3d])
        db.session.commit()

        #region
        amazon = Region(
            sat_id = 1, #landsat_id,
            name = "Amazon Rainforest",
            latitude = -3.4653,
            longitude = -62.2159,
        )
        sahara = Region(
            sat_id = 1, #landsat_id,
            name = "Sahara Desert",
            latitude = 23.4162,
            longitude = 25.6628,
        )
        east_coast = Region(
            sat_id = 2, #geos_id,
            name = "East Coast(US)",
            latitude = 35.2271,
            longitude = -80.8431,
        )
        mexico_gulf = Region(
            sat_id = 2, #geos_id,
            name = "Gulf of Mexico",
            latitude = 25.00,
            longitude = -90.00,
        )
        great_barrier_reef = Region(
            sat_id = 3, #sentinel_id,  
            name = "Great Barrier Reef",
            latitude = -18.2871,
            longitude = 147.6992,
        )
        himalayas = Region(
            sat_id = 3, #sentinel_id,  
            name = "Himalayas",
            latitude = 27.9881,
            longitude = 86.9250,
        )
        philippine_sea = Region(
            sat_id = 4, #himawari_id,  
            name = "Philippine Sea",
            latitude = 15.0,
            longitude = 130.0,
        )
        antarctica = Region(
            sat_id = 5,#terra_id,
            name = "Antarctica",
            latitude = -75.2500,
            longitude = -0.0714,
        )
        greenland = Region(
            sat_id = 6,#aqua_id,  
            name = "Greenland Ice Sheet",
            latitude = 71.7069,
            longitude = -42.6043,
        )
        andes_mountains = Region(
            sat_id = 7,#cosmo_sky_id,
            name = "Andes Mountains",
            latitude = -32.6532,
            longitude = -70.0115,
        )
        indian_ocean = Region(
            sat_id = 8,#insat_3d_id,
            name = "Indian Ocean",
            latitude = -10.0,
            longitude = 80.0,
        )
        hurricane_zone = Region(
            sat_id = 8,#insat_3d_id,
            name = "Hurricane Formation Zone",
            latitude = 12.5,
            longitude = -60.0,
        )

        db.session.add_all([amazon, sahara, east_coast, mexico_gulf, great_barrier_reef, himalayas, philippine_sea, antarctica, greenland, andes_mountains, indian_ocean, hurricane_zone])
        db.session.commit()

        #sat data
        surface_temp = SatelliteData(
            sat_id = 1,#landsat_id,
            data_type = "Surface Temperature",
            data_value = "32°c",
            date_recorded = date(2024, 12, 27),
        )
        vegetation_index = SatelliteData(
            sat_id = 1,#landsat_id,
            data_type = "NDVI(Veg Index)",
            data_value = "0.75",
            date_recorded = date(2025, 3, 9),
        )
        cloud_cover = SatelliteData(
            sat_id = 2,#geos_id,
            data_type = "Cloud Cover",
            data_value = "65%",
            date_recorded = date(2025, 2, 10),
        )
        wind_speed = SatelliteData(
            sat_id = 2,#geos_id,
            data_type = "Wind Speed",
            data_value = "120 km/h",
            date_recorded = date(2025, 3, 6),
        )
        ocean_temp = SatelliteData(
            sat_id = 3,#sentinel_id,  
            data_type = "Sea Surface Temperature",
            data_value = "28°C",
            date_recorded = date(2025, 1, 15),
        )
        air_quality = SatelliteData(
            sat_id = 3,#sentinel_id,  
            data_type = "Air Quality Index",
            data_value = "AQI 42 (Good)",
            date_recorded = date(2025, 2, 5),
        )
        hurricane_intensity = SatelliteData(
            sat_id = 4,#himawari_id,  
            data_type = "Hurricane Intensity",
            data_value = "Category 4",
            date_recorded = date(2025, 3, 8),
        )
        ozone_levels = SatelliteData(
            sat_id = 5,#terra_id,  
            data_type = "Ozone Concentration",
            data_value = "290 DU",
            date_recorded = date(2025, 3, 10),
        )
        sea_level_rise = SatelliteData(
            sat_id = 6,#aqua_id,  
            data_type = "Sea Level Rise",
            data_value = "3.2 mm/year",
            date_recorded = date(2025, 1, 20),
        )
        polar_ice_extent = SatelliteData(
            sat_id = 6,#aqua_id,  
            data_type = "Polar Ice Extent",
            data_value = "12.5 million km²",
            date_recorded = date(2025, 2, 18),
        )
        earthquake_detection = SatelliteData(
            sat_id=7,#cosmo_sky_id,  
            data_type="Ground Displacement",
            data_value="5.3 cm shift",
            date_recorded=date(2025, 3, 5),
        )
        solar_radiation = SatelliteData(
            sat_id = 8,#insat_3d_id,  
            data_type = "Solar Radiation",
            data_value = "1361 W/m²",
            date_recorded = date(2025, 2, 25),
        )
        precipitation_rate = SatelliteData(
            sat_id = 8,#insat_3d_id,  
            data_type = "Precipitation Rate",
            data_value = "15 mm/hr",
            date_recorded = date(2025, 3, 12),
        )

        db.session.add_all([surface_temp, vegetation_index, cloud_cover, wind_speed, ocean_temp, air_quality, hurricane_intensity, ozone_levels, sea_level_rise, polar_ice_extent, earthquake_detection, solar_radiation, precipitation_rate])
        db.session.commit()



