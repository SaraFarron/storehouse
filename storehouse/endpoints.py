from flask_restful import fields
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
        Get user
        ---
        tags:
          - user
        parameters:
          - in: json
            name: id
            required: true
            type: integer
        responses:
          200:
            schema:
              $ref: '#/definitions/User'
          404:
            description: User with this id was not found
            schema: {'error': 'object not found'}
        """
        return super(UserEndpoints, self).get(model_id)

    def put(self, model_id):
        """
        Update user
        ---
        tags:
          - user
        parameters:
          - in: json
            name: id
            required: true
            type: integer
        responses:
          200:
            schema:
              $ref: '#/definitions/User'
          404:
            description: User with this id was not found
            schema: {'error': 'object not found'}
        """
        return super(UserEndpoints, self).put(model_id)

    def patch(self, model_id):
        """
        Partial update user
        ---
        tags:
          - user
        parameters:
          - in: json
            name: id
            required: true
            type: integer
        responses:
          200:
            schema:
              $ref: '#/definitions/User'
          404:
            description: User with this id was not found
            schema: {'error': 'object not found'}
        """
        return super(UserEndpoints, self).patch(model_id)

    def delete(self, model_id):
        """
        Delete user
        ---
        tags:
          - user
        parameters:
          - in: json
            name: id
            required: true
            type: integer
        responses:
          204:
            schema:
              $ref: '#/definitions/User'
          404:
            description: User with this id was not found
            schema: {'error': 'object not found'}
        """
        return super(UserEndpoints, self).delete(model_id)


class VideoEndpoints(GenericEndpoints):
    model = Video
    model_fields = video_fields

    def get(self, model_id):
        """
        Get video
        ---
        tags:
          - video
        parameters:
          - in: json
            name: id
            required: true
            type: integer
        responses:
          200:
            schema:
              $ref: '#/definitions/Video'
          404:
            description: Video with this id was not found
            schema: {'error': 'object not found'}
        """
        return super(VideoEndpoints, self).get(model_id)

    def put(self, model_id):
        """
        Update video
        ---
        tags:
          - video
        parameters:
          - in: json
            name: id
            required: true
            type: integer
        responses:
          200:
            schema:
              $ref: '#/definitions/Video'
          404:
            description: Video with this id was not found
            schema: {'error': 'object not found'}
        """
        return super(VideoEndpoints, self).put(model_id)

    def patch(self, model_id):
        """
        Partial update video
        ---
        tags:
          - video
        parameters:
          - in: json
            name: id
            required: true
            type: integer
        responses:
          200:
            schema:
              $ref: '#/definitions/Video'
          404:
            description: Video with this id was not found
            schema: {'error': 'object not found'}
        """
        return super(VideoEndpoints, self).patch(model_id)

    def delete(self, model_id):
        """
        Delete video
        ---
        tags:
          - video
        parameters:
          - in: json
            name: id
            required: true
            type: integer
        responses:
          204:
            schema:
              $ref: '#/definitions/Video'
          404:
            description: Video with this id was not found
            schema: {'error': 'object not found'}
        """
        return super(VideoEndpoints, self).delete(model_id)


class VideosEndpoints(GenericsEndpoints):
    model = Video
    model_fields = video_fields

    def get(self):
        """
        Get all videos
        ---
        tags:
          - video
        responses:
          200:
            description: All users data
            schema:
              $ref: '#/definitions/Video'
        """
        return super(VideosEndpoints, self).get()

    def post(self):
        """
        Create a new video
        ---
        tags:
          - video
        parameters:
          - in: json
            name: title
            required: true
            description: video title
            type: string
          - in: json
            name: owner_id
            required: true
            description: owner id, User foreign key
            type: integer
          - in: json
            name: episodes
            description: number of episodes
            type: integer
            default: 1
          - in: json
            name: is_series
            type: boolean
          - in: json
            name: franchise_id
            description: franchise id, foreign key to Franchise
            type: integer
          - in: json
            name: order_number
            description: order number in franchise
            type: integer
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
          - watchlist
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
          - watchlist
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
          - franchise
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
          - franchise
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
