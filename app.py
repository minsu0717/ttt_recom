from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from config import Config
from rating import MovieRecommandResource

app = Flask(__name__)
CORS(app)

app.config.from_object(Config)

jwt = JWTManager(app)

api = Api(app)

api.add_resource(MovieRecommandResource,'/6')

if __name__=='__main__':
    app.run()
