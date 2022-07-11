from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api


app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
from storehouse import endpoints, models

api.add_resource(endpoints.UserEndpoints, '/user/<int:model_id>')
api.add_resource(endpoints.UsersEndpoints, '/users')

api.add_resource(endpoints.VideoEndpoints, '/video/<int:model_id>')
api.add_resource(endpoints.VideosEndpoints, '/videos')

api.add_resource(endpoints.WatchlistEndpoints, '/watchlist/<int:model_id>')
api.add_resource(endpoints.WatchlistsEndpoints, '/watchlists')

api.add_resource(endpoints.FranchiseEndpoints, '/franchise/<int:model_id>')
api.add_resource(endpoints.FranchisesEndpoints, '/franchises')
