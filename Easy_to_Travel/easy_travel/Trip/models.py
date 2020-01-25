from config import db

class Trip(db.Model):
    trId = db.Column('tr_id',db.Integer(),primary_key=True)
    trScr = db.column('tr_scr',db.String(100))
    trDes = db.column('tr_des',db.String(100))
    trDate = db.Column('tr_date',db.Integer())
    trDriver = db.Column('tr_driver',db.ForeignKey('driver.driver_id'),unique=True)
    trvehicle = db.Column('tr_vehicle',db.ForeignKey('vehicle.vehicle_id'),unique=False)
