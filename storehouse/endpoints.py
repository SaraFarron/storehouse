import jwt
from flask import request, jsonify, make_response
from flask_restful import fields
from datetime import datetime, timedelta
from functools import wraps
from werkzeug.security import check_password_hash

from storehouse import app
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


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({'message': 'Token is missing !!'}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = User.query.filter_by(public_id=data['public_id']).first()
        except:  # TODO make tokens expirable
            return jsonify({
                'message': 'Token is invalid !!'
            }), 401

        return f(current_user, *args, **kwargs)

    return decorated


@app.route('/users/login', methods=['POST'])
def login():
    """
    Login endpoint, use this to get your token
    ---
    tags:
      - auth
    parameters:
      - name: email
        in: json
        type: string
        required: true
      - name: password
        in: json
        type: string
        required: true
    responses:
      201:
        description: successful authentication
      401:
        description: email and password required
      401:
        description: wrong email or password
      404:
        description: user not found
    """
    auth = request.get_json(force=True)

    if not all([auth, auth.get('email'), auth.get('password')]):
        return make_response(
            'Could not verify',
            401,
            {'WWW-Authenticate': 'Basic realm ="Login required!"'}
        )

    user = User.query.filter_by(email=auth.get('email')).first()
    if not user:
        return make_response(
            'Could not verify',
            404,
            {'WWW-Authenticate': 'Basic realm ="User does not exist!"'}
        )

    if check_password_hash(user.password, auth.get('password')):
        token = jwt.encode({
            'public_id': user.public_id,
            'exp': datetime.utcnow() + timedelta(minutes=30)
        }, app.config['SECRET_KEY'])
        return make_response(jsonify({'token': token}), 201)

    return make_response(
        'Could not verify',
        403,
        {'WWW-Authenticate': 'Basic realm ="Wrong Password!"'}
    )


@app.route('/users/signup', methods=['POST'])
def signup():
    """
    Registration endpoint, use this to create a new user
    ---
    tags:
      - auth
    parameters:
      - name: name
        in: json
        type: string
        required: true
      - name: email
        in: json
        type: string
        required: true
      - name: password
        in: json
        type: string
        required: true
    responses:
      201:
        description: successful registration
      202:
        description: user already exists
    """
    args = request.get_json(force=True)
    user = User.query.filter_by(email=args['email']).first()
    if not user:
        User.create(args)
        return make_response('Successfully registered.', 201)
    return make_response('User already exists. Please Log in.', 202)


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
        return {'error': 'To create a user use /users/signup endpoint!'}, 400


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

    @token_required
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

    @token_required
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

    @token_required
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

    @token_required
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

    @token_required
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

    @token_required
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

    @token_required
    def get(self):
        """
        Get all videos
        ---
        tags:
          - video
        responses:
          200:
            description: All videos data
            schema:
              $ref: '#/definitions/Video'
        """
        return super(VideosEndpoints, self).get()

    @token_required
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
        responses:
          201:
            schema:
              $ref: '#/definitions/Video'
        """
        return super(VideosEndpoints, self).post()


class WatchlistEndpoints(GenericEndpoints):
    model = Watchlist
    model_fields = watchlist_fields

    @token_required
    def get(self, model_id):
        """
        Get watchlist
        ---
        tags:
          - watchlist
        parameters:
          - in: json
            name: id
            required: true
            type: integer
        responses:
          200:
            schema:
              $ref: '#/definitions/Watchlist'
          404:
            description: Watchlist with this id was not found
            schema: {'error': 'object not found'}
        """
        return super(WatchlistEndpoints, self).get(model_id)

    @token_required
    def put(self, model_id):
        """
        Update watchlist
        ---
        tags:
          - watchlist
        parameters:
          - in: json
            name: id
            required: true
            type: integer
        responses:
          200:
            schema:
              $ref: '#/definitions/Watchlist'
          404:
            description: Watchlist with this id was not found
            schema: {'error': 'object not found'}
        """
        return super(WatchlistEndpoints, self).put(model_id)

    @token_required
    def patch(self, model_id):
        """
        Partial update watchlist
        ---
        tags:
          - watchlist
        parameters:
          - in: json
            name: id
            required: true
            type: integer
        responses:
          200:
            schema:
              $ref: '#/definitions/Watchlist'
          404:
            description: Watchlist with this id was not found
            schema: {'error': 'object not found'}
        """
        return super(WatchlistEndpoints, self).patch(model_id)

    @token_required
    def delete(self, model_id):
        """
        Delete watchlist
        ---
        tags:
          - watchlist
        parameters:
          - in: json
            name: id
            required: true
            type: integer
        responses:
          200:
            schema:
              $ref: '#/definitions/Watchlist'
          404:
            description: Watchlist with this id was not found
            schema: {'error': 'object not found'}
        """
        return super(WatchlistEndpoints, self).delete(model_id)


class WatchlistsEndpoints(GenericsEndpoints):
    model = Watchlist
    model_fields = watchlist_fields

    def get(self):
        """
        Get all watchlists
        ---
        tags:
          - watchlist
        responses:
          200:
            description: All watchlists data
            schema:
              $ref: '#/definitions/Watchlist'
        """
        return super(WatchlistsEndpoints, self).get()

    @token_required
    def post(self):
        """
        Create a new watchlist
        ---
        tags:
          - watchlist
        parameters:
          - in: json
            name: user_id
            required: true
            description: User foreign key
            type: integer
          - in: json
            name: target_id
            description: Watchlist foreign key
            required: true
            type: integer
          - in: json
            name: score
            required: true
            type: float
          - in: json
            name: rewatches
            type: integer
        """
        return super(WatchlistsEndpoints, self).post()


class FranchiseEndpoints(GenericEndpoints):
    model = Franchise
    model_fields = franchise_fields

    def get(self, model_id):
        """
        Get franchise
        ---
        tags:
          - franchise
        parameters:
          - in: json
            name: id
            required: true
            type: integer
        responses:
          200:
            schema:
              $ref: '#/definitions/Franchise'
          404:
            description: Franchise with this id was not found
            schema: {'error': 'object not found'}
        """
        return super(FranchiseEndpoints, self).get(model_id)

    @token_required
    def put(self, model_id):
        """
        Update franchise
        ---
        tags:
          - franchise
        parameters:
          - in: json
            name: id
            required: true
            type: integer
        responses:
          200:
            schema:
              $ref: '#/definitions/Franchise'
          404:
            description: Franchise with this id was not found
            schema: {'error': 'object not found'}
        """
        return super(FranchiseEndpoints, self).put(model_id)

    @token_required
    def patch(self, model_id):
        """
        Parital update franchise
        ---
        tags:
          - franchise
        parameters:
          - in: json
            name: id
            required: true
            type: integer
        responses:
          200:
            schema:
              $ref: '#/definitions/Franchise'
          404:
            description: Franchise with this id was not found
            schema: {'error': 'object not found'}
        """
        return super(FranchiseEndpoints, self).patch(model_id)

    @token_required
    def delete(self, model_id):
        """
        Get franchise
        ---
        tags:
          - franchise
        parameters:
          - in: json
            name: id
            required: true
            type: integer
        responses:
          200:
            schema:
              $ref: '#/definitions/Franchise'
          404:
            description: Franchise with this id was not found
            schema: {'error': 'object not found'}
        """
        return super(FranchiseEndpoints, self).delete(model_id)


class FranchisesEndpoints(GenericsEndpoints):
    model = Franchise
    model_fields = franchise_fields

    @token_required
    def get(self):
        """
        Get all franchises
        ---
        tags:
          - franchise
        responses:
          200:
            description: All franchises data
            schema:
              $ref: '#/definitions/Franchise'
        """
        return super(FranchisesEndpoints, self).get()

    @token_required
    def post(self):
        """
        Create a new franchise
        ---
        tags:
          - franchise
        parameters:
          - in: json
            name: name
            required: true
            type: string
        responses:
          201:
            schema:
              $ref: '#/definitions/Franchise'
        """
        return super(FranchisesEndpoints, self).post()
