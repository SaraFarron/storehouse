from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_migrate import Migrate
from flasgger import Swagger


app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SWAGGER'] = {
    'title': 'Storehouse API',
    'uiversion': 3,
}
db = SQLAlchemy(app)
migrate = Migrate(app, db)
swag = Swagger(app, template_file='docs/template.yml')
from storehouse import endpoints, models

api.add_resource(endpoints.UserEndpoints, '/user/<int:model_id>')
api.add_resource(endpoints.UsersEndpoints, '/users')

api.add_resource(endpoints.VideoEndpoints, '/video/<int:model_id>')
api.add_resource(endpoints.VideosEndpoints, '/videos')

api.add_resource(endpoints.WatchlistEndpoints, '/watchlist/<int:model_id>')
api.add_resource(endpoints.WatchlistsEndpoints, '/watchlists')

api.add_resource(endpoints.FranchiseEndpoints, '/franchise/<int:model_id>')
api.add_resource(endpoints.FranchisesEndpoints, '/franchises')
