from flask_restful import Resource
from flask import request

from flask_jwt_extended import jwt_required,get_jwt_identity
from models.merchant import Merchant

class CdnAuthenticationApi(Resource):
    """needed by sayom shakib for his cdn, accepts bearer token, returns user_id"""


    @jwt_required
    def post(self):

        current_user = get_jwt_identity()
        user=Merchant.query.get_or_404(current_user,description="INVALID USER")

        return {"merchant_id":current_user},200