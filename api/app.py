from flask import Flask, request
from flask_restful import Resource, Api

from models import app
from resources.login import LoginResource
from resources.register import RegisterResource

api = Api(app)

class HelloWorld(Resource):
    def get(self):
        jenis = ['R', 'G', 'B']
        return {'jenis': jenis}


    def delete(self):
        global warna
        warna.remove('red')
        return {'warna':warna}

    def post(self):
        return {'warna':warna}

api.add_resource(HelloWorld, '/')
api.add_resource(LoginResource, '/login')
api.add_resource(RegisterResource, '/register')

if __name__ == '__main__':
    app.run(debug=True)

