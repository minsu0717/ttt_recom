from flask import Flask, request
# JWT 사용을 위한 SECRET_KEY 정보가 들어있는 파일 임포트
from config import Config
from flask.json import jsonify
from http import HTTPStatus
from flask_restful import Api
from flask_jwt_extended import JWTManager
from resources.movie import AddFavoriteResource, DeleteFavoriteResource, FavoriteListResource, MovieInfoResource, MovieListResource, MovieSearchResource
from resources.login import UserLoginResource
from resources.rating import MovieRecommandResource, MovieRecommandResource_1

from resources.register import UserRegisterResource
from resources.logout import UserLogoutResource, jwt_blacklist
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# 환경변수 셋팅
app.config.from_object(Config)

# JWT 토큰 만들기
jwt = JWTManager(app)

# todo : 로그아웃 개발하고 나서, 코멘트 해제한다.
@jwt.token_in_blocklist_loader
def check_if_token_is_revoked(jwt_header, jwt_payload) :
    jti = jwt_payload['jti']
    return jti in jwt_blacklist

api = Api(app)

# 경로와 리소스를 연결한다.
api.add_resource(UserRegisterResource, '/api/register')
api.add_resource(UserLoginResource, '/api/login')
api.add_resource(UserLogoutResource, '/api/v1/user/logout')
api.add_resource(MovieListResource,'/api/movie')
api.add_resource(MovieInfoResource,'/5/<int:movie_id>')
api.add_resource(MovieSearchResource,'/1')
api.add_resource(AddFavoriteResource,'/2/<int:movie_id>')
api.add_resource(FavoriteListResource,'/4')
api.add_resource(DeleteFavoriteResource,'/3/<int:movie_id>')
api.add_resource(MovieRecommandResource,'/6')
api.add_resource(MovieRecommandResource_1,'/7')


if __name__ == '__main__' :
    app.run(host='0.0.0.0',port=5001)