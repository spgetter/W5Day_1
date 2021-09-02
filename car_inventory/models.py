from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import uuid 
from datetime import datetime

# Adding Flask Security for Passwords
from werkzeug.security import generate_password_hash, check_password_hash

# Import Secrets Module (Given by Python)
import secrets

# Imports for Login Manager and Flask Login
from flask_login import UserMixin, LoginManager

# Imports for Flask Marshmallow
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
lm = LoginManager()
ma = Marshmallow()

@lm.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.String(150), primary_key = True)
    first_name = db.Column(db.String(150), nullable = True, default = '')
    last_name = db.Column(db.String(150), nullable = True, default = '')
    email = db.Column(db.String(150), nullable = False)
    password = db.Column(db.String, nullable = True, default = '')
    g_auth_verify = db.Column(db.Boolean, default = False)
    token = db.Column(db.String, default = '', unique = True)
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    car = db.relationship('Car', backref = 'owner', lazy = True)

    def __init__(self, email, first_name = '', last_name = '', id='', password='', token='', g_auth_verify = False):
        self.id = self.set_id()
        self.first_name = first_name
        self.last_name = last_name
        self.password = self.set_password(password)
        self.email = email
        self.token = self.set_token(24)
        self.g_auth_verify = g_auth_verify

    def set_token(self,length):
        return secrets.token_hex(length)

    def set_id(self):
        return str(uuid.uuid4())

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

    def __repr__(self):
        return f'User {self.email} has been added to the database.'

class Car(db.Model):
    id = db.Column(db.String, primary_key = True)
    make = db.Column(db.String(150))
    _model = db.Column(db.String(200))
    year = db.Column(db.String(10))
    price = db.Column(db.Numeric(precision=10, scale=2))
    seats = db.Column(db.String(150), nullable = True)
    transmission = db.Column(db.String(100), nullable = True)
    engine = db.Column(db.String(100))
    dimensions = db.Column(db.String(100))
    weight = db.Column(db.String(100))
    MSRP = db.Column(db.Numeric(precision=10,scale=2))
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)

    def __init__(self,make,_model,year,price,seats,transmission,engine,dimensions,weight,MSRP,user_token,id=''):
        self.id = self.set_id()
        self.make = make
        self._model = _model
        self.year = year
        self.price = price
        self.seats = seats
        self.transmission = transmission
        self.engine = engine
        self.dimensions = dimensions
        self.weight = weight
        self.MSRP = MSRP
        self.user_token = user_token

    def __repr__(self):
        return f'The following car has been added: {self.name}'

    def set_id(self):
        return (secrets.token_urlsafe())

# Creation of api schema via the marshmallow object
class CarSchema(ma.Schema):
    class Meta:
        fields = ['id', 'make','_model','year','price','seats','transmission', 'engine', 'dimensions','weight','MSRP']

car_schema = CarSchema()
cars_schema = CarSchema(many=True)