from datetime import date
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Satellite(db.Model):
    
    __tablename__ = "satellites"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    _orbit_type = db.Column("orbit_type", db.String, nullable=False) # info: LEO,MEO,GEO
    _status = db.Column("status", db.String, nullable=False) # info: active, inactive
    description = db.Column(db.String, nullable=False)
    image_url = db.Column(db.String)
    country = db.Column(db.String, nullable=False, default='Unknown')

    regions = db.relationship("Region", back_populates="satellite", lazy="selectin", cascade="all, delete-orphan")
    satellite_data = db.relationship("SatelliteData", back_populates="satellite", lazy="selectin", cascade="all, delete-orphan")

    def __repr__(self):
        return f"Satellite(id: {self.id}, name: {self.name}, orbit_type: {self.orbit_type}, status: {self.status}, description: {self.description}, image_url: {self.image_url}, country: {self.country})"
       
    @property
    def status(self):
        return self._status
    @status.setter
    def status(self, status) -> None:
        if status in ["active", "inactive"]:
            self._status = status
        else:
            raise ValueError(f"{status} is Invalid! 'active' or 'inactive' allowed only") 
    
    @property
    def orbit_type(self):
        return self._orbit_type
    @orbit_type.setter
    def orbit_type(self, orbit_type) -> None:
        if orbit_type in ["LEO", "MEO", "GEO"]:
            self._orbit_type = orbit_type
        else:
            raise ValueError(f"{orbit_type} is Invalid! 'MEO', 'LEO', 'GEO' allowed only")
        
class SatelliteData(db.Model):

    __tablename__ = "satellite_data"

    id = db.Column(db.Integer, primary_key=True)
    sat_id = db.Column(db.Integer, db.ForeignKey("satellites.id"), nullable=False)
    _data_type = db.Column("data_type", db.String, nullable=False)
    data_value = db.Column(db.String, nullable=False)
    date_recorded = db.Column(db.Date, default=date.today) 
   
    satellite = db.relationship("Satellite", back_populates="satellite_data")

    def __repr__(self):
        return f"SatelliteData(id: {self.id},sat_id: {self.sat_id}, data_type: {self.data_type}, data_value: {self.data_value}, date_recorded: {self.date_recorded})"

    #note: This property is just here to fill project requirements
    @property
    def data_type(self):
        return self._data_type
    @data_type.setter
    def data_type(self, data_type):
        if isinstance(data_type, str):
            self._data_type = data_type
        else:
            raise ValueError(f"{data_type} is not an String")

class Region(db.Model):

    __tablename__ = "regions"

    id = db.Column(db.Integer, primary_key=True)
    sat_id = db.Column(db.Integer, db.ForeignKey("satellites.id"), nullable=False)
    name = db.Column(db.String, nullable=False)
    _latitude = db.Column("latitude", db.Float)
    _longitude = db.Column("longitude", db.Float)
    
    satellite = db.relationship("Satellite", back_populates="regions")

    def __repr__(self):
        return f"Region(id: {self.id}, sat_id: {self.sat_id}, name: {self.name}, latitude: {self.latitude}, longitude: {self.longitude})"
    
    @property
    def latitude(self):
        return self._latitude
    @latitude.setter
    def latitude(self, latitude):
        if isinstance(latitude, float):
            self._latitude = latitude
        else:
            raise ValueError(f"{latitude} is not a float")
    
    @property
    def longitude(self):
        return self._longitude
    @longitude.setter
    def longitude(self, longitude):
        if isinstance(longitude, float):
            self._longitude = longitude
        else:
            raise ValueError(f"{longitude} is not a float")



