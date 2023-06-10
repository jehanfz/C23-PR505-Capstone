from flask import jsonify
from flask_restful import Resource, reqparse

from models import User

parser = reqparse.RequestParser()
parser.add_argument('email', type=str)
parser.add_argument('username', type=str)
parser.add_argument('password', type=str)

class RegisterResource(Resource):
    def post(self):
        data = parser.parse_args()
        email = data['email']
        username = data['username']
        password = data['password']

        if not email or not username or not password:
            response = jsonify({'message': 'Email, Username, Password tidak boleh kosong.'})
            response.status_code = 400
            return response

        user_exists = User.fetch(email)

        if user_exists:
            response = jsonify({'message': 'Email sudah terdaftar'})
            response.status_code = 400
            return response

        user = User.create(email, username, password)
        response = jsonify({'username': username, 'email': email})
        response.status_code = 200
        return response