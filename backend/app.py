from flask import Flask, jsonify, request
from mydb.models import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///monitoring.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db.init_app(app)

from mydb.models import Satellite, SatelliteData, Region


@app.route('/')
def home():
    return jsonify({"message": "Satellite Monitoring API is running"})

# mark: satellite table 
@app.route("/satellites", methods=["GET"])
def get_satellites():
    satellites = Satellite.query.all()
    return jsonify([{
        "id": sat.id,
        "name": sat.name,
        "orbit_type": sat.orbit_type,
        "status": sat.status,
        "description": sat.description
    } for sat in satellites])

@app.route("/satellites", methods=["POST"])
def add_satellite():
    data = request.json
    new_sat = Satellite(
        name=data['name'], 
        orbit_type=data['orbit_type'],
        status=data['status'],
        description=data['description']
        )
    
    db.session.add(new_sat)
    db.session.commit()
    return jsonify({"message": "Satellite added!"})

@app.route("/satellites/<int:id>", methods=["PUT"])
def edit_satellite(id):
    data = request.json
    sat = Satellite.query.get(id)

    if not sat:
        return jsonify({"message": "Satellite not found"}), 404
    
    sat.name = data.get('name', sat.name)
    sat.orbit_type = data.get('orbit_type', sat.orbit_type)
    sat.status = data.get('status', sat.status)
    sat.description = data.get('description', sat.description)

    db.session.commit()
    return jsonify({"message": "Satellite updated!"})

@app.route('/satellites/<int:id>', methods=['DELETE'])
def delete_satellite(id):
    sat = Satellite.query.get(id)

    if not sat:
        return jsonify({"message": "Satellite not found"}), 404
    
    db.session.delete(sat)
    db.session.commit()

    return jsonify({"message": "Satellite deleted!"})



#mark: data table 
@app.route("/satellites-data", methods=["GET"])
def get_data():
    satellite_data = SatelliteData.query.all()
    return jsonify([{
        "id": data.id,
        "sat_id": data.sat_id,
        "data_type": data.data_type,
        "data_value": data.data_value,
        "date_recorded": data.date_recorded
    } for data in satellite_data])


@app.route("/satellites-data", methods=["POST"])
def add_data():
    data = request.json
    new_data = SatelliteData(
        sat_id=data['sat_id'], 
        data_type=data['data_type'],
        data_value=data['data_value'],
        date_recorded=data['date_recorded']
        )
    
    db.session.add(new_data)
    db.session.commit()
    return jsonify({"message": "Satellite Data added!"})

@app.route("/satellites-data/<int:id>", methods=["PUT"])
def edit_data(id):
    data = request.json
    sat_data = SatelliteData.query.get(id)

    if not sat_data:
        return jsonify({"message": "Satellite Data not found"}), 404
    
    sat_data.sat_id = data.get('sat_id', sat_data.sat_id)
    sat_data.data_type = data.get('data_type', sat_data.data_type)
    sat_data.data_value = data.get('data_value', sat_data.data_value)
    sat_data.date_recorded = data.get('date_recorded', sat_data.date_recorded)

    db.session.commit()
    return jsonify({"message": "Satellite Data updated!"})

@app.route('/satellites-data/<int:id>', methods=['DELETE'])
def delete_data(id):
    sat_data = SatelliteData.query.get(id)

    if not sat_data:
        return jsonify({"message": "Satellite Data not found"}), 404
    
    db.session.delete(sat_data)
    db.session.commit()

    return jsonify({"message": "Satellite Data deleted!"})


#mark region table 
@app.route("/regions", methods=["GET"])
def get_regions():
    regions = Region.query.all()
    return jsonify([{
        "id": reg.id,
        "sat_id": reg.sat_id,
        "name": reg.name,
        "latitude": reg. latitude,
        "longitude": reg.longitude
    } for reg in regions])

@app.route("/regions", methods=["POST"])
def add_region():
    data = request.json
    new_reg = Region(
        sat_id=data['sat_id'], 
        name=data['name'],
        latitude=data['latitude'],
        longitude=data['longitude']
        )
    
    db.session.add(new_reg)
    db.session.commit()
    return jsonify({"message": "Region added!"})

@app.route("/regions/<int:id>", methods=["PUT"])
def edit_region(id):
    data = request.json
    region = Region.query.get(id)

    if not region:
        return jsonify({"message": "Region not found"}), 404
    
    region.sat_id = data.get('sat_id', region.sat_id)
    region.name = data.get('name', region.name)
    region.latitude = data.get('latitude', region.latitude)
    region.longitude = data.get('longitude', region.longitude)

    db.session.commit()
    return jsonify({"message": "Region updated!"})

@app.route('/regions/<int:id>', methods=['DELETE'])
def delete_region(id):
    region = Region.query.get(id)

    if not region:
        return jsonify({"message": "Region not found"}), 404
    
    db.session.delete(region)
    db.session.commit()

    return jsonify({"message": "Region deleted!"})


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)
