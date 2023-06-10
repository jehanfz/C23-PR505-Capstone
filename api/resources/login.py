from flask import jsonify
from flask_restful import Resource, reqparse

from models import User

parser = reqparse.RequestParser()
parser.add_argument('email', type=str)
parser.add_argument('password', type=str)

class LoginResource(Resource):
    def post(self):
        data = parser.parse_args()
        email = data['email']
        password = data['password']

        if not email or not password:
            response = jsonify({'message': 'Email dan Password tidak boleh kosong.'})
            response.status_code = 400
            return response

        user_exists = User.fetch(email)

        if user_exists:
            print(user_exists.password)
            if user_exists.check_password(password):
                response = jsonify({'message': 'Berhasil Login'})
                response.status_code = 200
                return response
            else:
                response = jsonify({'message': 'Password salah'})
                response.status_code = 400
                return response
        else:
            response = jsonify({'message': 'Email tidak terdaftar'})
            response.status_code = 400
            return response