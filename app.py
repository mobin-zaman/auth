from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager
from marshmallow import ValidationError
from flask_migrate import Migrate

from db import db
from ma import ma
from blacklist import BLACKLIST

from resources.user import TestDeploymentWorking, MerchantAuthenticationApi, TokenRefresh, MerchantLogout,CheckTokenValidity
from resources.cdn import CdnAuthenticationApi
from resources.test_resource import TestApi

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://username:password@localhost/test_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["JWT_BLACKLIST_ENABLED"] = True  # enable blacklist feature
app.config["JWT_SECRET_KEY"] = "ekta gopon kotha"
app.config["JWT_BLACKLIST_TOKEN_CHECKS"] = [
    "access",
    "refresh",
]  # allow blacklisting for access and refresh tokens
app.secret_key = "jose"  # could do app.config['JWT_SECRET_KEY'] if we prefer
api = Api(app)
jwt = JWTManager(app)
migrate = Migrate(app, db)


@app.before_first_request
def create_tables():
    db.create_all()


@app.errorhandler(ValidationError)
def handle_marshmallow_validation(err):
    return jsonify(err.messages), 400

@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decypted_token):
    return decypted_token["jti"] in BLACKLIST


api.add_resource(TestDeploymentWorking,
                 '/')  # just for testing the deployment!, doesn't guarantee functionality of the app
api.add_resource(MerchantAuthenticationApi, '/auth/')
api.add_resource(TokenRefresh, '/refresh/')
api.add_resource(MerchantLogout,'/logout/')
api.add_resource(CheckTokenValidity,'/check_validity/') #internal
api.add_resource(CdnAuthenticationApi,'/cdnauth/')


api.add_resource(TestApi,'/test/')




if __name__ == "__main__":
    db.init_app(app)
    ma.init_app(app)
    app.run('0.0.0.0',port=5000, debug=True)
