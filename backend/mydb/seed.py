from mydb.models import db, Satellite, SatelliteData, Region
from sqlalchemy import select
from datetime import date

db.create_all()

db.session.query(Satellite).delete()
db.session.query(Region).delete()
db.session.query(SatelliteData).delete()
db.session.commit()

# mark: CREATE
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

def add_sat(sat_name, sat_orbit_type, sat_status, sat_description):
    instance = Satellite(
        name = sat_name,
        orbit_type = sat_orbit_type,
        status = sat_status,
        description = sat_description
    )
    db.session.add(instance)
    db.session.commit()     

db.session.add_all([landsat, geos, sentinel, himawari, terra, aqua, cosmo_sky, insat_3d])
db.session.commit()

#region
amazon = Region(
    sat_id = landsat_id,
    name = "Amazon Rainforest",
    latitude = -3.4653,
    longitude = -62.2159,
)
sahara = Region(
    sat_id = landsat_id,
    name = "Sahara Desert",
    latitude = 23.4162,
    longitude = 25.6628,
)
east_coast = Region(
    sat_id = geos_id,
    name = "East Coast(US)",
    latitude = 35.2271,
    longitude = -80.8431,
)
mexico_gulf = Region(
    sat_id = geos_id,
    name = "Gulf of Mexico",
    latitude = 25.00,
    longitude = -90.00,
)
great_barrier_reef = Region(
    sat_id = sentinel_id,  
    name = "Great Barrier Reef",
    latitude = -18.2871,
    longitude = 147.6992,
)
himalayas = Region(
    sat_id = sentinel_id,  
    name = "Himalayas",
    latitude = 27.9881,
    longitude = 86.9250,
)
philippine_sea = Region(
    sat_id = himawari_id,  
    name = "Philippine Sea",
    latitude = 15.0,
    longitude = 130.0,
)
antarctica = Region(
    sat_id = terra_id,
    name = "Antarctica",
    latitude = -75.2500,
    longitude = -0.0714,
)
greenland = Region(
    sat_id = aqua_id,  
    name = "Greenland Ice Sheet",
    latitude = 71.7069,
    longitude = -42.6043,
)
andes_mountains = Region(
    sat_id = cosmo_sky_id,
    name = "Andes Mountains",
    latitude = -32.6532,
    longitude = -70.0115,
)
indian_ocean = Region(
    sat_id = insat_3d_id,
    name = "Indian Ocean",
    latitude = -10.0,
    longitude = 80.0,
)
hurricane_zone = Region(
    sat_id = insat_3d_id,
    name = "Hurricane Formation Zone",
    latitude = 12.5,
    longitude = -60.0,
)

def add_region(sat_idx, reg_name, reg_latitude, reg_longitude):
    instance = Region(
        sat_id = sat_idx,
        name = reg_name,
        latitude = reg_latitude,
        longitude = reg_longitude
    )
    db.session.add(instance)
    db.session.commit() 

db.session.add_all([amazon, sahara, east_coast, mexico_gulf, great_barrier_reef, himalayas, philippine_sea, antarctica, greenland, andes_mountains, indian_ocean, hurricane_zone])
db.session.commit()

#sat data
surface_temp = SatelliteData(
    sat_id = landsat_id,
    data_type = "Surface Temperature",
    data_value = "32°c",
    date_recorded = date(2024, 12, 27),
)
vegetation_index = SatelliteData(
    sat_id = landsat_id,
    data_type = "NDVI(Veg Index)",
    data_value = "0.75",
    date_recorded = date(2025, 3, 9),
)
cloud_cover = SatelliteData(
    sat_id = geos_id,
    data_type = "Cloud Cover",
    data_value = "65%",
    date_recorded = date(2025, 2, 10),
)
wind_speed = SatelliteData(
    sat_id = geos_id,
    data_type = "Wind Speed",
    data_value = "120 km/h",
    date_recorded = date(2025, 3, 6),
)
ocean_temp = SatelliteData(
    sat_id = sentinel_id,  
    data_type = "Sea Surface Temperature",
    data_value = "28°C",
    date_recorded = date(2025, 1, 15),
)
air_quality = SatelliteData(
    sat_id = sentinel_id,  
    data_type = "Air Quality Index",
    data_value = "AQI 42 (Good)",
    date_recorded = date(2025, 2, 5),
)
hurricane_intensity = SatelliteData(
    sat_id = himawari_id,  
    data_type = "Hurricane Intensity",
    data_value = "Category 4",
    date_recorded = date(2025, 3, 8),
)
ozone_levels = SatelliteData(
    sat_id = terra_id,  
    data_type = "Ozone Concentration",
    data_value = "290 DU",
    date_recorded = date(2025, 3, 10),
)
sea_level_rise = SatelliteData(
    sat_id = aqua_id,  
    data_type = "Sea Level Rise",
    data_value = "3.2 mm/year",
    date_recorded = date(2025, 1, 20),
)
polar_ice_extent = SatelliteData(
    sat_id = aqua_id,  
    data_type = "Polar Ice Extent",
    data_value = "12.5 million km²",
    date_recorded = date(2025, 2, 18),
)
earthquake_detection = SatelliteData(
    sat_id=cosmo_sky_id,  
    data_type="Ground Displacement",
    data_value="5.3 cm shift",
    date_recorded=date(2025, 3, 5),
)
solar_radiation = SatelliteData(
    sat_id = insat_3d_id,  
    data_type = "Solar Radiation",
    data_value = "1361 W/m²",
    date_recorded = date(2025, 2, 25),
)
precipitation_rate = SatelliteData(
    sat_id = insat_3d_id,  
    data_type = "Precipitation Rate",
    data_value = "15 mm/hr",
    date_recorded = date(2025, 3, 12),
)

def add_data(sat_idx, type_data, value_data, date):
    instance = SatelliteData(
        sat_id = sat_idx,
        data_type = type_data,
        data_value = value_data,
        date_recorded = date
    )
    db.session.add(instance)
    db.session.commit() 

db.session.add_all([surface_temp, vegetation_index, cloud_cover, wind_speed, ocean_temp, air_quality, hurricane_intensity, ozone_levels, sea_level_rise, polar_ice_extent, earthquake_detection, solar_radiation, precipitation_rate])
db.session.commit()




#mark: READ
# read satellites
def get_sats():
    stmt = select(Satellite)
    sat_result = db.session.execute(stmt).scalars()
    return list(sat_result)

def get_sat_ids():
    sat_objs = get_sats()
    return [sat.id for sat in sat_objs]

def get_active_sat():
    sat_objs = get_sats()
    return [sat for sat in sat_objs if sat.status == "active"]

# read region
def get_reg():
    stmt = select(Region)
    region_result = db.session.execute(stmt).scalars()
    return list(region_result)

def get_reg_ids():
    reg_objs = get_reg()
    return [reg.id for reg in reg_objs]
#read sat data
def get_data():
    stmt = select(SatelliteData)
    data_result = db.session.execute(stmt).scalars()
    return list(data_result)

def get_data_type():
    data_objs = get_data()
    return [data.data_type for data in data_objs]

def get_data_ids():
    data_objs = get_data()
    return [data.id for data in data_objs]




# mark UPDATE

# info: update satellite
# stmt = select(Satellite).where(Satellite.id == 1 )
# sat1 = session.scalars(stmt).first()
# sat1.name = "Not Landsat-9"
# session.commit()

def update_sat(sat_id, variable, new_value):
    stmt = select(Satellite).where(Satellite.id == sat_id )
    sat = db.session.scalars(stmt).first()
    if sat:
        setattr(sat, variable, new_value)
        db.session.commit()
    else:
        print(f"There is no Satellite of Id {sat_id}")


# info: update region
# stmt = select(Region).where(Region.id == 1 )
# region1 = session.scalars(stmt).first()
# region1.name = "Not Amazon"
# session.commit()

def update_region(reg_id, variable, new_value):
    stmt = select(Region).where(Region.id == reg_id )
    reg = db.session.scalars(stmt).first()
    if reg:
        setattr(reg, variable, new_value)
        db.session.commit()
    else:
        print(f"There is no Region of Id {reg_id}")

# info: update data
# stmt = select(SatelliteData).where(SatelliteData.id == 1 )
# data1 = session.scalars(stmt).first()
# data1.name = "Not Surface Temperature"
# session.commit()

def update_data(data_id, variable, new_value):
    stmt = select(SatelliteData).where(SatelliteData.id == data_id )
    data = db.session.scalars(stmt).first()
    if data:
        setattr(data, variable, new_value)
        db.session.commit()
    else:
        print(f"There is no Satellite Data of Id {data_id}")




# mark: DELETE
# info: delete satellite
# session.delete(landsat)
# session.delete(geos)
# session.commit()

# def delete_landsat():
#     session.delete(landsat)
#     session.commit()

# def delete_geos():
#     session.delete(geos)
#     session.commit()

def delete_sat(user_id):
    stmt = select(Satellite).where(Satellite.id == user_id)
    sat_result = db.session.execute(stmt).scalars().first()
    if sat_result:
        db.session.delete(sat_result)
        db.session.commit()

# info: delete region
#session.delete(amazon)
#session.delete(sahara)
#session.delete(east_coast)
#session.delete(mexico_gulf)
#session.commit()

def delete_region(user_id):
    stmt = select(Region).where(Region.id == user_id)
    region_result = db.session.execute(stmt).scalars().first()
    if region_result:
        db.session.delete(region_result)
        db.session.commit()


# info: delete data
#session.delete(surface_temp)
#session.delete(vegetation_index)
#session.delete(cloud_cover)
#session.delete(wind_speed)
#session.commit()

def delete_data(user_id):
    stmt = select(SatelliteData).where(SatelliteData.id == user_id)
    data_result = db.session.execute(stmt).scalars().first()
    if data_result:
        db.session.delete(data_result)
        db.session.commit()
