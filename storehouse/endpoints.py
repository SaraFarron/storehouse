from flask_restful import Resource, reqparse, fields, marshal_with
from storehouse.models import User, Video, Watchlist, Franchise
from storehouse import db


parser = reqparse.RequestParser()
parser.add_argument('name', required=True)
parser.add_argument('email', required=True)
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
        args = parser.parse_args()
        User.create(args)


class UserEndpoints(Resource):
    @marshal_with(user_fields)
    def get(self, user_id):
        user = User.get(user_id)
        return user, 200

    def put(self, user_id):
        args = parser.parse_args()
        try:
            User.update(user_id, args)
        except AssertionError:
            User.create(args)
        return '', 201

    def patch(self, user_id):
        pass

    def delete(self, user_id):
        user = User.get(user_id)
        db.session.delete(user)
        db.session.commit()
        return '', 204
