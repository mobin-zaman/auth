from marshmallow import Schema,fields

class BusniessUrl(Schema):
    id = fields.Integer()
    name = fields.String()
    api_endpoint=fields.String()