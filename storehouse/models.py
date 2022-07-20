from datetime import date
from werkzeug.security import generate_password_hash

from storehouse import db


class CRUDs:
    @classmethod
    def get(cls, model_id: int):
        return cls.query.get(model_id)

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def create(cls, fields: dict):
        entry = cls(**fields)
        db.session.add(entry)
        db.session.commit()

    @classmethod
    def update(cls, model_id: int, fields: dict):
        entry = cls.get(model_id)
        assert entry, 'User not found'
        fields = {k: v for k, v in fields.items() if v}
        for field, value in fields.items():
            setattr(entry, field, value)
        db.session.commit()

    @classmethod
    def delete(cls, model_id: int):
        db.session.delete(cls.query.get(model_id))
        db.session.commit()


class User(db.Model, CRUDs):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    watchlist = db.relationship('Watchlist', backref='user', lazy=True)
    uploads = db.relationship('Video', backref='owner', lazy=True)

    @classmethod
    def create(cls, fields: dict):
        fields['password'] = generate_password_hash(fields['password'])
        super(User, cls).create(fields)

    def __repr__(self):
        return f'User(id={self.id} name={self.name} email={self.email})'


class Watchlist(db.Model, CRUDs):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    target_id = db.Column(db.Integer, db.ForeignKey('video.id'), nullable=False)
    target_type = db.Column(db.String(10))
    score = db.Column(db.Float)
    episodes = db.Column(db.Integer, nullable=False)
    rewatches = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'Watchlist(id={self.id} user_id={self.user_id} target_id={self.target_id})'


class Franchise(db.Model, CRUDs):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    titles = db.relationship('Video', backref='franchise', lazy=True)

    def __repr__(self):
        return f'Franchise(id={self.id} name={self.name})'


class Video(db.Model, CRUDs):
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    franchise_id = db.Column(db.Integer, db.ForeignKey('franchise.id'))
    title = db.Column(db.String(50), nullable=False)
    episodes = db.Column(db.Integer, default=1)
    is_series = db.Column(db.Boolean, default=False, nullable=False)
    upload_date = db.Column(db.Date, default=date.today, nullable=False)
    score = db.Column(db.Float, default=0, nullable=False)
    duration = db.Column(db.Float, nullable=False)
    order_number = db.Column(db.Integer)
    watchlists = db.relationship('Watchlist', backref='target', lazy=True)

    def __repr__(self):
        return f'Video(id={self.id} title={self.title})'


# db.create_all() Needed on first run
