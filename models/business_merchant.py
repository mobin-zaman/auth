from models import business,merchant
from db import db
from sqlalchemy.dialects.mysql import BIGINT, TINYINT


business_merchant = db.Table('business_merchant',
                             db.Column('id', BIGINT(unsigned=True), primary_key=True),
                             db.Column('business_id', BIGINT(unsigned=True),primary_key=True),
                             db.Column('role'), TINYINT(unsigned=True)
                             )

