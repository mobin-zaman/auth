from marshmallow import Schema, fields, validate
from .business_schema import BusniessUrl



class MerchantSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)



