from db import db
from sqlalchemy.dialects.mysql import BIGINT
from models import business_merchant

class Business(db.Model):
    
    id = db.Column(BIGINT(unsigned=True),primary_key=True)
    name = db.Column(db.String(255))
    owner_name=db.Column(db.String(255))
    billing_address=db.Column(db.Text)
    geo_lat=db.Column(db.Float)
    geo_long=db.Column(db.Float)
    billing_phone=db.Column(db.String(20))
    billing_email=db.Column(db.String(127))
    logo_id =db.Column(BIGINT(unsigned=True)) #FIXME: HERE SHOULD BE A RELATIONSHIP
    cover_id=db.Column(BIGINT(unsigned=True))
    open_time=db.Column(db.Time)
    close_time=db.Column(db.Time)
    api_endpoint:db.Column(db.String(255))
    bot_app_id=db.Column(BIGINT(unsigned=True))
    bot_url=db.Column(db.String(127))
    page_id=db.Column(BIGINT(unsigned=True))
    page_url=db.Column(db.String(127))
    inserted_on=db.Column(db.TIMESTAMP)
    updated_on=db.Column(db.TIMESTAMP)

#FIXME: NEED BUSINESS MARCHANT TABLE






