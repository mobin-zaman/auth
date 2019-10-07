from db import db
from sqlalchemy.dialects.mysql import BIGINT
from passlib.hash import bcrypt as bc
from models import business_merchant


class Merchant(db.Model):

    id = db.Column(BIGINT(unsigned=True), primary_key=True)
    name = db.Column(db.String(80))
    username = db.Column(db.String(20), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(20))
    email = db.Column(db.String(127), unique=True)
    role = db.Column(db.SmallInteger)
    passphrase = db.Column(db.String(255))
    profile_photo_url = db.Column(db.String(127))
    inserted_on = db.Column(db.TIMESTAMP) #FIXME: add default timestamp here
    updated_on = db.Column(db.TIMESTAMP) #FIXME: ^ as mentoined above

    def __repr__(self):
        return "<User {} {}".format(self.username, self.password_hash)

    def __init__(self, username, password, passphrase):
        self.username = username
        self.password_hash = bc.using(13).hash(password)
        self.passphrase = passphrase

    @classmethod
    def find_by_username(cls, username) -> "MerchantModel":
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, id) -> "MerchantModel":
        return cls.query.filter_by(id=id).first()

    def verify_password(self, password):
        return bc.verify(password, self.password_hash)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    # def delete_from_db
