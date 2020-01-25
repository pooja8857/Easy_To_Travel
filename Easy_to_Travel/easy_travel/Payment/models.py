from config import db

class Payment(db.Model):
    payId = db.Column('pay_id',db.Integer(),primary_key=True)
    payMode = db.Column('pay_mode',db.String(50))
    payAmt = db.Column('pay_amt',db.LongInt())
    payCustid = db.Column('pay_custid',db.ForeignKey('customer.cust_id'),unique=False)#doubt in unique
    payVehicle = db.Column('pay_vehicle',db.ForeignKey('vehicle.veh_id'),unique=False)#doubt in unique
    payHistory = db.relationship('History', uselist=False, lazy=True, backref='payhist')