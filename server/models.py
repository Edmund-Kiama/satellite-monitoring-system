from datetime import date
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin
from flask_migrate import Migrate
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.json.compact = False

db = SQLAlchemy()
db.init_app(app)

migrate = Migrate(app, db)

class Satellite(db.Model, SerializerMixin):
    __tablename__ = "satellites"
    serialize_rules=("-regions","-satellite_data")

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    orbit_type = db.Column("orbit_type", db.String, nullable=False) # info: LEO,MEO,GEO, Lunar, Solar orbit
    status = db.Column("status", db.String, nullable=False) # info: active, inactive
    description = db.Column(db.String, nullable=False)
    image_url = db.Column(db.String)
    country = db.Column(db.String, nullable=False)

    altitude = db.Column(db.String ,nullable=False)
    speed = db.Column(db.String, nullable=False)
    launch_date = db.Column(db.Date)
    type = db.Column(db.String, nullable=False)

    regions = db.relationship("Region", back_populates="satellite", lazy="selectin", cascade="all, delete-orphan")
    satellite_data = db.relationship("SatelliteData", back_populates="satellite", lazy="selectin", cascade="all, delete-orphan")

    def __repr__(self):
        return f"Satellite(id: {self.id}, name: {self.name}, orbit_type: {self.orbit_type}, status: {self.status}, description: {self.description}, image_url: {self.image_url}, country: {self.country})"
    
    @validates("status")
    def validate_status(self, key, status):
        if status not in ["active", "inactive"]:
            raise ValueError(f"{key} is Invalid! 'active' or 'inactive' allowed only") 
        return status
    
    @validates("orbit_type")
    def validate_orbit_type(self, key, orbit_type):
        if orbit_type not in ["LEO", "MEO", "GEO", "Lunar", "Solar orbit"]:
            raise ValueError(f"{key} is Invalid! 'MEO', 'LEO', 'GEO', 'Lunar', 'Solar orbit' allowed only")
        return orbit_type

class SatelliteData(db.Model, SerializerMixin):
    __tablename__ = "satellite_data"
    serialize_rules = ("-satellite",)

    id = db.Column(db.Integer, primary_key=True)
    sat_id = db.Column(db.Integer, db.ForeignKey("satellites.id"), nullable=False)
    data_type = db.Column("data_type", db.String, nullable=False)
    data_value = db.Column(db.String, nullable=False)
    date_recorded = db.Column(db.Date, default=date.today) 

    data_accuracy = db.Column(db.String,nullable=False)
    measurement_unit = db.Column(db.String,nullable=False)
    source = db.Column(db.String, nullable=False)
    satellite_orbit = db.Column(db.String, nullable=False)

    satellite = db.relationship("Satellite", back_populates="satellite_data")

    def __repr__(self):
        return f"SatelliteData(id: {self.id},sat_id: {self.sat_id}, data_type: {self.data_type}, data_value: {self.data_value}, date_recorded: {self.date_recorded})"

    @validates("data_type")
    def validate_data_type(self, key, data):
        if not isinstance(data, str):
            raise ValueError(f"{key} must be a string")
        return data

class Region(db.Model, SerializerMixin):
    __tablename__ = "regions"
    serialize_rules = ("-satellite",)

    id = db.Column(db.Integer, primary_key=True)
    sat_id = db.Column(db.Integer, db.ForeignKey("satellites.id"), nullable=False)
    name = db.Column(db.String, nullable=False)
    latitude = db.Column("latitude", db.Float)
    longitude = db.Column("longitude", db.Float)

    area = db.Column(db.String, nullable=False)
    climate_type = db.Column(db.String, nullable=False)
    primary_focus = db.Column(db.String, nullable=False)

    satellite = db.relationship("Satellite", back_populates="regions")

    def __repr__(self):
        return f"Region(id: {self.id}, sat_id: {self.sat_id}, name: {self.name}, latitude: {self.latitude}, longitude: {self.longitude})"
    
    @validates("latitude", "longitude")
    def validate(self, key, val):
        if not isinstance(val, float):
            raise ValueError(f"{key} must be a float")
        return val