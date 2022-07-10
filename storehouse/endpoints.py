from flask_restful import Resource, reqparse, fields, marshal_with
from storehouse.models import User, Video, Watchlist, Franchise
from storehouse import db
from sqlalchemy.exc import IntegrityError


user_parser = reqparse.RequestParser()
user_parser.add_argument('name')
user_parser.add_argument('email')
user_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'email': fields.String,
}

video_parser = reqparse.RequestParser()
video_parser.add_argument()
video_fields = {}


class GenericEndpoints(Resource):
    model = None
    model_fields = None
    model_parser = None

    @marshal_with(model_fields)
    def get(self, model_id):
        instance = self.model.get(model_id)
        return instance, 200

    def put(self, model_id):
        args = self.model_parser.parse_args()
        try:
            self.model.update(model_id, args)
        except AssertionError:
            self.model.create(args)
        return '', 201

    def patch(self, model_id):
        args = self.model_parser.parse_args()
        try:
            self.model.update(model_id, args)
        except AssertionError:
            return {'error': 'object not found'}, 404
        return '', 200

    def delete(self, model_id):
        self.model.delete(model_id)
        return '', 204


class UsersEndpoints(Resource):
    @marshal_with(user_fields)
    def get(self):
        return User.get_all(), 200

    def post(self):
        args = user_parser.parse_args()
        try:
            User.create(args)
        except IntegrityError:
            return {'error': 'user with this email already exists'}, 400
        return '', 201


class UserEndpoints(GenericEndpoints):
    model = User
    model_fields = user_fields
    model_parser = user_parser


class VideoEndpoints(GenericEndpoints):
    model = Video
    model_fields = video_fields
    model_parser = video_parser


class VideosEndpoints(Resource):
    pass
