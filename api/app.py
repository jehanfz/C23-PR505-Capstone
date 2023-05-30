from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

warna = ['red','green','blue']


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

if __name__ == '__main__':
    app.run(debug=True)