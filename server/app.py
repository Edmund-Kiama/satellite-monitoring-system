from flask import request, make_response
from models import db, Satellite, SatelliteData, Region, app
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

@app.errorhandler(404)
def not_found(e):
    return make_response({"message": "404 Not Found"}, 404)

@app.route('/')
def home():
    return make_response({"message": "Satellite Monitoring API is running"}, 201)

# mark: satellite table 
@app.route("/satellites", methods=["GET"])
def get_satellites():
    satellites = Satellite.query.all()
    return make_response([sat.to_dict() for sat in satellites], 201)

@app.route("/satellites", methods=["POST"])
def add_satellite():
    try:
        data = request.json
    
        data['launch_date'] =  datetime.strptime(data["launch_date"], "%Y-%m-%d").date()

        new_sat = Satellite(
            name=data['name'], 
            orbit_type=data['orbit_type'],
            status=data['status'],
            description=data['description'],
            image_url=data['image_url'],
            country=data['country'],
            altitude=data['altitude'],
            speed=data['speed'],
            type=data['type'],
            launch_date=data['launch_date']
            )

        db.session.add(new_sat)
        db.session.commit()

        return make_response({"message": "Satellite added!"}, 201)
    
    except:
        return make_response({"message": "Error occurred"}, 400)

@app.route("/satellites/<int:id>", methods=["PUT"])
def edit_satellite(id):
    data = request.json

    if not data:
            return make_response({"Error: Invalid request"}, 400)
    
    sat = Satellite.query.get(id)

    if not sat:
        return make_response({"message": "Satellite not found"}, 404)
    
    sat.name = data.get('name', sat.name)
    sat.orbit_type = data.get('orbit_type', sat.orbit_type)
    sat.status = data.get('status', sat.status)
    sat.description = data.get('description', sat.description)
    sat.image_url = data.get('image_url', sat.image_url)
    sat.country = data.get('country', sat.country)
    sat.altitude = data.get('altitude', sat.altitude)
    sat.speed = data.get('speed', sat.speed)
    sat.type = data.get('type', sat.type)

    date_str = data.get('launch_date')
    date_object = datetime.strptime(date_str, '%Y-%m-%d').date()
    sat.launch_date = date_object

    db.session.commit()

    return make_response({"message": "Satellite updated!"}, 201)

@app.route('/satellites/<int:id>', methods=['DELETE'])
def delete_satellite(id):
    sat = Satellite.query.get(id)

    if not sat:
        return make_response({"message": "Satellite not found"}, 404)
    
    db.session.delete(sat)
    db.session.commit()

    return make_response({"message": "Satellite deleted!"}, 201)


#mark: data table 
@app.route("/satellites-data", methods=["GET"])
def get_data():
    satellite_data = SatelliteData.query.all()

    return make_response([data.to_dict() for data in satellite_data], 201)

@app.route("/satellites-data", methods=["POST"])
def add_data():
    data = request.json

    data['date_recorded'] =  datetime.strptime(data["date_recorded"], "%Y-%m-%d").date()

    new_data = SatelliteData(
        sat_id=data['sat_id'], 
        data_type=data['data_type'],
        data_value=data['data_value'],
        date_recorded=data['date_recorded'],
        data_accuracy=data['data_accuracy'],
        measurement_unit=data['measurement_unit'],
        source=data['source'],
        satellite_orbit=data['satellite_orbit']
        )
    
    db.session.add(new_data)
    db.session.commit()

    return make_response({"message": "Satellite Data added!"}, 201)

@app.route("/satellites-data/<int:id>", methods=["PUT"])
def edit_data(id):
    data = request.json
    sat_data = SatelliteData.query.get(id)

    if not sat_data:
        return make_response({"message": "Satellite Data not found"}, 404)
    
    sat_data.sat_id = data.get('sat_id', sat_data.sat_id)
    sat_data.data_type = data.get('data_type', sat_data.data_type)
    sat_data.data_value = data.get('data_value', sat_data.data_value)

    date_str = data.get('date_recorded')
    date_object = datetime.strptime(date_str, '%Y-%m-%d').date()
    sat_data.date_recorded = date_object

    sat_data.data_accuracy = data.get('data_accuracy', sat_data.data_accuracy)
    sat_data.measurement_unit = data.get('measurement_unit', sat_data.measurement_unit)
    sat_data.source = data.get('source', sat_data.source)
    sat_data.satellite_orbit = data.get('satellite_orbit', sat_data.satellite_orbit)

    db.session.commit()

    return make_response({"message": "Satellite Data updated!"}, 201)

@app.route('/satellites-data/<int:id>', methods=['DELETE'])
def delete_data(id):
    sat_data = SatelliteData.query.get(id)

    if not sat_data:
        return make_response({"message": "Satellite Data not found"}, 404)

    db.session.delete(sat_data)
    db.session.commit()

    return make_response({"message": "Satellite Data deleted!"}, 201)

#mark region table 
@app.route("/regions", methods=["GET"])
def get_regions():
    regions = Region.query.all()
    return make_response([reg.to_dict() for reg in regions], 201)

@app.route("/regions", methods=["POST"])
def add_region():
    data = request.json

    new_reg = Region(
        sat_id=data['sat_id'], 
        name=data['name'],
        latitude=data['latitude'],
        longitude=data['longitude'],
        area=data['area'],
        climate_type=data['climate_type'],
        primary_focus=data['primary_focus']
        )
    
    db.session.add(new_reg)
    db.session.commit()

    return make_response({"message": "Region added!"}, 201)

@app.route("/regions/<int:id>", methods=["PUT"])
def edit_region(id):
    data = request.json
    region = Region.query.get(id)

    if not region:
        return make_response({"message": "Region not found"}, 404)
    
    region.sat_id = data.get('sat_id', region.sat_id)
    region.name = data.get('name', region.name)
    region.latitude = data.get('latitude', region.latitude)
    region.longitude = data.get('longitude', region.longitude)
    
    region.area = data.get('area', region.area)
    region.climate_type = data.get('climate_type', region.climate_type)
    region.primary_focus = data.get('primary_focus', region.primary_focus)


    db.session.commit()

    return make_response({"message": "Region updated!"}, 201)

@app.route('/regions/<int:id>', methods=['DELETE'])
def delete_region(id):
    region = Region.query.get(id)

    if not region:
        return make_response({"message": "Region not found"}, 404)
    
    db.session.delete(region)
    db.session.commit()

    return make_response({"message": "Region deleted!"}, 201)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(port=5555, debug=True)

