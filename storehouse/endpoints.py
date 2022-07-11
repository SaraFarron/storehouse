from flask_restful import Resource, reqparse, fields, marshal, marshal_with
from storehouse.models import User, Video, Watchlist, Franchise
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
video_parser.add_argument('owner_id', type=int)
video_parser.add_argument('title')
video_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'owner_id': fields.Integer,
    'episodes': fields.Integer,
    'is_series': fields.Boolean,
    'upload_date': fields.DateTime,
    'score': fields.Float,
}
franchise_parser = reqparse.RequestParser()
franchise_parser.add_argument('name')
franchise_fields = {
    'id': fields.Integer,
    'name': fields.String,
}
watchlist_parser = reqparse.RequestParser()
watchlist_parser.add_argument('user_id')
watchlist_fields = {
    'id': fields.Integer,
    'user_id': fields.Integer,
    'target_id': fields.Integer,
    'score': fields.Float,
    'episodes': fields.Integer,
    'rewatches': fields.Integer,
}


class GenericEndpoints(Resource):
    model = None
    model_fields = None
    model_parser = None

    def get(self, model_id):
        instance = self.model.get(model_id)
        return marshal(instance, self.model_fields), 200

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


class WatchlistEndpoints(GenericEndpoints):
    pass


class WatchlistsEndpoints(Resource):
    pass


class FranchiseEndpoints(GenericEndpoints):
    pass


class FranchisesEndpoints(Resource):
    pass
