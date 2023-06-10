from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@localhost:3306/batik"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "4a72e70144b77601baeff6fab3a8462a"
app.config['SECURITY_PASSWORD_SALT'] = "0mS5uWVCHu2SXLnA3XPEDA"

db = SQLAlchemy()
db.init_app(app)

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)

    @staticmethod
    def fetch(email=None):
        return User.query.filter_by(email=email).first()

    @staticmethod
    def create(email, username, password):
        password = generate_password_hash(password, method="pbkdf2:sha256", salt_length=8)
        user = User(email=email, username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return User.fetch(email)

    def check_password(self, password):
        return check_password_hash(self.password, password)