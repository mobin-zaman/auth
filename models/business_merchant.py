from models import business,merchant
from db import db
from sqlalchemy.dialects.mysql import BIGINT, TINYINT


business_merchant = db.Table('business_merchant',
                             db.Column('id', BIGINT(unsigned=True), primary_key=True),
                             db.Column('user_id', BIGINT(unsigned=True),db.ForeignKey('merchant.id'),nullable=False),
                             db.Column('business_id', BIGINT(unsigned=True),db.ForeignKey('business.id'),nullable=False),
                             db.Column('role', TINYINT(unsigned=True)), #0 owner 1 manager 2 sales
                             )

