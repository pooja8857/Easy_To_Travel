from config import db

class Customer(db.Model):
    custId=db.Column('cust_id',db.Integer(),primary_key=True)
    custName=db.Column('cust_name',db.String(100))
    custDOB=db.Column('cust_dob',db.Integer(100))
    custEmail = db.Column('cust_email',db.String(100))
    custmobileno =db.Column('cust_cno',db.Integer())
    custVehicle = db.relationship('Vehicle',uselist=True,lazy=True,backref='custveh')
    custHistory = db.relationship('History',uselist=False,lazy=True,backref='custhist')
    custPayment = db.relationship('Payment',uselist=False,lazy=True,backref='custpay')
    custAddress = db.relationship('Address',uselist=True,
                              secondary='cust_adr',lazy='subquery',
                              backerf=db.backref('cust_adr',lazy=True))
