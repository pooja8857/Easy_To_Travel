from config import db

cust_adr=db.Table('cust_adr',
                  db.column('custId',db.Integer(),db.ForeignKey('Customer.cust_id'),unique=False,primary_key=True),
                  db.column('adrId',db.Integer(),db.ForeignKey('Address.adr_id'),unique=False,primary_key=True))

class Address(db.Model):
    adrId=db.Column('adr_id',db.Integer(),primary_key=True)
    adrCity=db.Column('adress_City',db.String(100))
    adrState=db.Column('adress_State',db.String(100))
    adrPincode=db.Column('adress_pin',db.Integer())
    ownerId = db.Column('ownadr_id',db.ForeignKey('owner.owner_id'),unique=False,nullable=True)
