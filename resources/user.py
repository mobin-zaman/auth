from flask_restful import Resource
from flask import request
from schemas.user_schema import MerchantSchema

from flask_jwt_extended import create_refresh_token, create_access_token,get_jwt_identity,jwt_refresh_token_required,jwt_required,get_raw_jwt
from blacklist import BLACKLIST
from models.merchant import MerchantModel
from .custom_hash import match_hash
import time


class TestDeploymentWorking(Resource):
    def get(self):
        return "working auth!"


class MerchantAuthenticationApi(Resource):
    """this is the external point"""
    """param: json {username, password}"""
    """return: accress_token,refresh_token,api_url_endpoint"""

    def post(self):
        json_input=request.get_json()
        print(json_input) #FIXME: delete this in production
        
        if not json_input:
            return {'errors':'bad request'},400

        data=MerchantSchema().load(json_input)
        print(data, data)

        user=MerchantModel.find_by_username(data['username'])

        if not user:
            return {'errors':'login invalid'},400

        if not user.verify_password(data['password']):
            return {'errors':'login invalid'},400

        access_token=create_access_token(identity=user.id,fresh=True)
        refresh_token=create_refresh_token(user.id)

        return {
            'access_token':access_token,
            'refresh_token':refresh_token,
        }


class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()

        MerchantModel.query.get_or_404(current_user) #this line will make sure the filteration of invalid access tokens


        access_token = create_access_token(identity=current_user)
        print('current: ', current_user)
        return {'access_token': access_token}



class MerchantLogout(Resource):
    @classmethod
    @jwt_required
    def post(cls):
        jti = get_raw_jwt()["jti"]  # jti is "JWT ID", a unique identifier for a JWT.
        BLACKLIST.add(jti)
        return {"message": "logout successful"}, 200




class CheckTokenValidity(Resource):
    @jwt_required #this will check the token validity
    def post(self):
        """
        it will take acces_token from the post as header 'Bearer JWT'
        and match the passphrase
        """

        current_user = get_jwt_identity()  # getting the user_id from jwt
        print("current: ",current_user)
        #FIXME: the bellow query needs more work to verify the existence of the user, we need to delete the inactive users
        user = MerchantModel.query.get_or_404(current_user, description="INVALID TOKEN") #Thanks Allah I thought of this test

        """stop man in the middle"""
        print("check 1")
        data = request.values
        print("check 2")
        print(data['timestamp'])
        print("check 3")
        request_time_stamp =float(data['timestamp'])

        elapsed = time.time()-request_time_stamp  # difference between two request's time

        if elapsed > 60:  # if the time delay of the request is greater than 60s
            return {"errors": "request time out"}, 400  # FIXME: fix the status codes

        """passphrase+timestamp=request_hash"""

        hash_matched = match_hash(data['timestamp'], user.passphrase,
                                              data['token'])  # the passphrase is taken from database
        print(data['token'])
        print(hash_matched)

        if not hash_matched:
            return {"erros": "INVALID REQUEST"}, 403
        """hash match"""
        """^ on the other side of the code, there will request.status!=200"""
        return {'msg': 'token valid'}, 200

