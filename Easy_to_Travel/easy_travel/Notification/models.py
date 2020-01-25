from config import db

class Notify(db.Model):
    notId=db.Column('not_id',db.Integer(),primary_key=True)
    notMsg=db.Column('not_msg',db.String(200))
