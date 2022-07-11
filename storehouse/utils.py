from flask_restful import Resource, marshal
from sqlalchemy.exc import IntegrityError


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


class GenericsEndpoints(Resource):
    model = None
    model_fields = None
    model_parser = None

    def get(self):
        return marshal(self.model.get_all(), self.model_fields), 200

    def post(self):
        args = self.model_parser.parse_args()
        try:
            self.model.create(args)
        except IntegrityError:
            return {'error': 'bad request'}, 400
        return '', 201
