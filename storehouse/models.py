from storehouse import db
from datetime import date


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    watchlist = db.relationship('Watchlist', backref='user', lazy=True)
    uploads = db.relationship('Video', backref='owner', lazy=True)


class Watchlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    target_id = db.Column(db.Integer, db.ForeignKey('video.id'), nullable=False)
    target_type = db.Column(db.String(10))
    score = db.Column(db.Float)
    episodes = db.Column(db.Integer, nullable=False)
    rewatches = db.Column(db.Integer, default=0)


class Franchise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titles = db.relationship('Video', backref='franchise', lazy=True)


class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    franchise_id = db.Column(db.Integer, db.ForeignKey('franchise.id'))
    title = db.Column(db.String(50), nullable=False)
    episodes = db.Column(db.Integer, default=1)
    is_series = db.Column(db.Boolean, default=False, nullable=False)
    upload_date = db.Column(db.Date, default=date.today, nullable=False)
    score = db.Column(db.Float, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    order_number = db.Column(db.Integer)
    watchlists = db.relationship('Watchlist', backref='target', lazy=True)
