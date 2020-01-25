from config import db

class History(db.Column):
    hisId = db.Column('his_id',db.Integer(),primary_key=True)
    hisCustid = db.Column('his_custid',db.ForeignKey('customer.cust_id'),unique=True)
    hisPayid = db.Column('his_payid',db.ForeignKey('Payment.pay_id'),unique=True)
    hisVehicle = db.Column('his_vehicle', db.ForeignKey('vehicle.veh_id'), unique=False)  # doubt in unique
    hisDriver = db.Column('his_driver', db.ForeignKey('driver.driver_id'), unique=False)  # doubt in unique

