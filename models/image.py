from db import db
from sqlalchemy.dialects.mysql import BIGINT,TINYINT,TIMESTAMP

class Images(db.Model):
    id=db.Column(BIGINT(unsigned=20),primary_key=True)
    url=db.Column(db.String(127))
    attachment_id=db.Column(BIGINT(unsigned=True))
    is_deleted=db.Column(TINYINT(1,unsigned=True))
    inserted_on=db.Column(TIMESTAMP)