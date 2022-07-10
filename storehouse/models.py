from storehouse import db
from datetime import date


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    # password = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    watchlist = db.relationship('Watchlist', backref='user', lazy=True)
    uploads = db.relationship('Video', backref='owner', lazy=True)

    @classmethod
    def get(cls, user_id: int):
        return cls.query.get(user_id)

    @classmethod
    def create(cls, fields: dict):
        user = User(
            name=fields['name'],
            email=fields['email'],
        )
        db.session.add(user)
        db.session.commit()

    @classmethod
    def update(cls, user_id: int, fields: dict):
        user = cls.get(user_id)
        assert user, 'User not found'
        fields = {k: v for k, v in fields.items() if v}
        for field, value in fields.items():
            setattr(user, field, value)
        db.session.commit()

    def __repr__(self):
        return f'User(id={self.id} name={self.name} email={self.email})'


class Watchlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    target_id = db.Column(db.Integer, db.ForeignKey('video.id'), nullable=False)
    target_type = db.Column(db.String(10))
    score = db.Column(db.Float)
    episodes = db.Column(db.Integer, nullable=False)
    rewatches = db.Column(db.Integer, default=0)

    @classmethod
    def get(cls, list_id: int):
        return cls.query.get(list_id)

    def __repr__(self):
        return f'Watchlist(id={self.id} user_id={self.user_id} target_id={self.target_id})'


class Franchise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # name = db.Column(db.String(30), nullable=False)
    titles = db.relationship('Video', backref='franchise', lazy=True)

    @classmethod
    def get_franchise(cls, franchise_id: int):
        return cls.query.get(franchise_id)

    # def __repr__(self):
    #     return f'Franchise(id={self.id} name={self.name})'


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

    @classmethod
    def get(cls, video_id: int):
        return cls.query.get(video_id)

    def __repr__(self):
        return f'Video(id={self.id} title={self.title})'
