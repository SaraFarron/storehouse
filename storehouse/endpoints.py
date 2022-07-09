from flask_restful import Resource, reqparse, fields, marshal_with
from storehouse.models import User, Video, Watchlist, Franchise
from storehouse import db


user_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'email': fields.String,
}


class UserEndpointSet(Resource):
    @marshal_with(user_fields)
    def get(self):
        users = User.query.all()
        return users, 200

    def post(self, name, email):
        user = User(
            name=name,
            email=email,
        )
        db.session.add(user)
        db.session.commit()
        return '', 201

    def put(self):
        pass

    def patch(self):
        pass

    def delete(self, user_id):
        user = User.query.get(user_id)
        db.session.delete(user)
        db.session.commit()
        return '', 204
