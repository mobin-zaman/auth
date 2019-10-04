from marshmallow import Schema, fields, validate



class MerchantSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True) 
