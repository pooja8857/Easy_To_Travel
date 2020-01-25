
from config import db

class Driver(db.Model):
    driId = db.Column('driver_id',db.Integer(),primary_key=True)
    driName = db.Column('driver_name',db.String(100))
    driDOB = db.Column('driver_dob',db.integer())
    driEmail = db.Column('driver_email', db.String(50))
    driMobile = db.Column('driver_cno',db.Integer())
    driLiscence = db.Column('driver_liscence',db.Integer())
    driAadhar = db.Column('driver_aadhar',db.LongInt())
    driRating = db.Column('driver_rating',db.Integer())
    driAddressProof =db.Column('driver_adrproof',db.String(100))
    vehicle = db.relationship('Vehicle',uselist=False,lazy=True,backref='driv_vehicle')
    ownerId = db.Column('owner_id',db.ForeignKey('owner.owner_id'),unique=False,nullable=True)
    driHistory = db.relationship('History', uselist=False, lazy=True, backref='drihist')
    driverTrip = db.relationship('Trip', uselist=False, lazy=True, backref='tripdriver')