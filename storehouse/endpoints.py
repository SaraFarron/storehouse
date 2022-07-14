from flask_restful import Resource, reqparse, fields
from storehouse.models import User, Video, Watchlist, Franchise
from storehouse.utils import GenericsEndpoints, GenericEndpoints


user_parser = reqparse.RequestParser()
user_parser.add_argument('name')
user_parser.add_argument('password')
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


class UsersEndpoints(GenericsEndpoints):
    model = User
    model_parser = user_parser
    model_fields = user_fields

    def get(self):
        """
        Get all users
        ---
        tags:
          - user
        responses:
          200:
            description: All users data
            schema:
              $ref: '#/definitions/Item'
        """
        return super(UsersEndpoints, self).get()


class UserEndpoints(GenericEndpoints):
    model = User
    model_fields = user_fields
    model_parser = user_parser


class VideoEndpoints(GenericEndpoints):
    model = Video
    model_fields = video_fields
    model_parser = video_parser


class VideosEndpoints(Resource):
    model = Video
    model_fields = video_fields
    model_parser = video_parser


class WatchlistEndpoints(GenericEndpoints):
    model = Watchlist
    model_fields = watchlist_fields
    model_parser = watchlist_parser


class WatchlistsEndpoints(Resource):
    model = Watchlist
    model_fields = watchlist_fields
    model_parser = watchlist_parser


class FranchiseEndpoints(GenericEndpoints):
    model = Franchise
    model_parser = franchise_parser
    model_fields = franchise_fields


class FranchisesEndpoints(Resource):
    model = Franchise
    model_parser = franchise_parser
    model_fields = franchise_fields
