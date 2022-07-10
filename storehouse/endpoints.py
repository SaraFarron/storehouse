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


class UsersEndpoints(Resource):
    @marshal_with(user_fields)
    def get(self):
        users = User.query.all()
        return users, 200

    def post(self):
        args = user_parser.parse_args()
        try:
            User.create(args)
        except IntegrityError:
            return {'error': 'user with this email already exists'}, 400
        return '', 201


class UserEndpoints(Resource):
    @marshal_with(user_fields)
    def get(self, user_id):
        user = User.get(user_id)
        return user, 200

    def put(self, user_id):
        args = user_parser.parse_args()
        try:
            User.update(user_id, args)
        except AssertionError:
            User.create(args)
        return '', 201

    def patch(self, user_id):
        args = user_parser.parse_args()
        try:
            User.update(user_id, args)
        except AssertionError:
            return {'error': 'user not found'}, 404
        return '', 200

    def delete(self, user_id):
        user = User.get(user_id)
        db.session.delete(user)
        db.session.commit()
        return '', 204
