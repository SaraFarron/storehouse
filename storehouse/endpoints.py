from flask_restful import Resource, fields
from storehouse.models import User, Video, Watchlist, Franchise
from storehouse.utils import GenericsEndpoints, GenericEndpoints


user_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'email': fields.String,
}
video_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'owner_id': fields.Integer,
    'episodes': fields.Integer,
    'is_series': fields.Boolean,
    'upload_date': fields.DateTime,
    'score': fields.Float,
}
franchise_fields = {
    'id': fields.Integer,
    'name': fields.String,
}
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
              $ref: '#/definitions/User'
        """
        return super(UsersEndpoints, self).get()

    def post(self):
        """
        Create a new user
        ---
        tags:
          - user
        parameters:
          - in: json
            name: name
            required: true
            description: The username
            type: string
          - in: json
            name: password
            required: true
            type: string
          - in: json
            name: email
            required: true
            type: string
        """
        return super(UsersEndpoints, self).post()


class UserEndpoints(GenericEndpoints):
    model = User
    model_fields = user_fields

    def get(self, model_id):
        """
        pass
        """
        return super(UserEndpoints, self).get(model_id)

    def put(self, model_id):
        """

        :param model_id:
        :return:
        """
        return super(UserEndpoints, self).put(model_id)

    def patch(self, model_id):
        """

        :param model_id:
        :return:
        """
        return super(UserEndpoints, self).patch(model_id)

    def delete(self, model_id):
        """

        :param model_id:
        :return:
        """
        return super(UserEndpoints, self).delete(model_id)


class VideoEndpoints(GenericEndpoints):
    model = Video
    model_fields = video_fields

    def get(self, model_id):
        """
        pass
        """
        return super(VideoEndpoints, self).get(model_id)

    def put(self, model_id):
        """

        :param model_id:
        :return:
        """
        return super(VideoEndpoints, self).put(model_id)

    def patch(self, model_id):
        """

        :param model_id:
        :return:
        """
        return super(VideoEndpoints, self).patch(model_id)

    def delete(self, model_id):
        """

        :param model_id:
        :return:
        """
        return super(VideoEndpoints, self).delete(model_id)


class VideosEndpoints(GenericsEndpoints):
    model = Video
    model_fields = video_fields

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
              $ref: '#/definitions/User'
        """
        return super(VideosEndpoints, self).get()

    def post(self):
        """
        Create a new user
        ---
        tags:
          - user
        parameters:
          - in: json
            name: name
            required: true
            description: The username
            type: string
          - in: json
            name: password
            required: true
            type: string
          - in: json
            name: email
            required: true
            type: string
        """
        return super(VideosEndpoints, self).post()


class WatchlistEndpoints(GenericEndpoints):
    model = Watchlist
    model_fields = watchlist_fields

    def get(self, model_id):
        """
        pass
        """
        return super(WatchlistEndpoints, self).get(model_id)

    def put(self, model_id):
        """

        :param model_id:
        :return:
        """
        return super(WatchlistEndpoints, self).put(model_id)

    def patch(self, model_id):
        """

        :param model_id:
        :return:
        """
        return super(WatchlistEndpoints, self).patch(model_id)

    def delete(self, model_id):
        """

        :param model_id:
        :return:
        """
        return super(WatchlistEndpoints, self).delete(model_id)


class WatchlistsEndpoints(GenericsEndpoints):
    model = Watchlist
    model_fields = watchlist_fields

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
              $ref: '#/definitions/User'
        """
        return super(WatchlistsEndpoints, self).get()

    def post(self):
        """
        Create a new user
        ---
        tags:
          - user
        parameters:
          - in: json
            name: name
            required: true
            description: The username
            type: string
          - in: json
            name: password
            required: true
            type: string
          - in: json
            name: email
            required: true
            type: string
        """
        return super(WatchlistsEndpoints, self).post()


class FranchiseEndpoints(GenericEndpoints):
    model = Franchise
    model_fields = franchise_fields

    def get(self, model_id):
        """
        pass
        """
        return super(FranchiseEndpoints, self).get(model_id)

    def put(self, model_id):
        """

        :param model_id:
        :return:
        """
        return super(FranchiseEndpoints, self).put(model_id)

    def patch(self, model_id):
        """

        :param model_id:
        :return:
        """
        return super(FranchiseEndpoints, self).patch(model_id)

    def delete(self, model_id):
        """

        :param model_id:
        :return:
        """
        return super(FranchiseEndpoints, self).delete(model_id)


class FranchisesEndpoints(GenericsEndpoints):
    model = Franchise
    model_fields = franchise_fields

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
              $ref: '#/definitions/User'
        """
        return super(FranchisesEndpoints, self).get()

    def post(self):
        """
        Create a new user
        ---
        tags:
          - user
        parameters:
          - in: json
            name: name
            required: true
            description: The username
            type: string
          - in: json
            name: password
            required: true
            type: string
          - in: json
            name: email
            required: true
            type: string
        """
        return super(FranchisesEndpoints, self).post()
