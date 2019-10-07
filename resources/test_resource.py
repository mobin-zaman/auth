from flask_restful import Resource
from models.business import Business
from models.merchant import Merchant
from schemas.user_schema import MerchantSchema

class TestApi(Resource):

    def get(self):
        user = Merchant.query.get(1)
        # data=MerchantSchema().dump(user)
        # return {'data':data}




