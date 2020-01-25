
from config import db

class Vehicle(db.Model):
    vehId = db.Column('veh_id',db.Integer(),primary_key=True)
    vehName = db.Column('veh_name',db.String(100))
    vehNo = db.Column('veh_no',db.Integer())
    vehSeater = db.Column('veh_seater',db.Integer())
    vehType = db.Column('veh_type',db.String(100))
    vehFueltype = db.Column('veh_fueltype',db.String(100))
    vehRC = db.Column('veh_rc',db.String(100))
    vehPermit = db.Column('veh_permit',db.String(100))
    vehInsurance = db.Column('veh_insurance',db.String(100))
    driverId = db.Column('driver_id',db.ForeignKey('driver.driver_id'),unique=True,nullable=True)
    ownerId = db.Column('owner_id',db.ForeignKey('owner.owner_id'),unique=False,nullable=True)
    custId = db.Column('cust_id',db.ForeignKey('customer.cust_id'),unique=False,nullable=True)
    vehTrip = db.relationship('Trip', uselist=True, lazy=True, backref='tripveh')
    vehHistory = db.relationship('History', uselist=False, lazy=True, backref='vehhist')
