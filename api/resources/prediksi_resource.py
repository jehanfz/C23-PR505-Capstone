import os
from flask import jsonify, request
from flask_restful import Resource

from prediksi import prediksi

class PrediksiResource(Resource):
    def post(self):
        file = request.files['gambar']
        if file:
            path = os.path.join('gambar', file.filename)
            file.save(path)
            rgb = prediksi(path)
            data = {'data': rgb}
            response = jsonify(data)
            response.status_code = 200
            return response
        else:
            response = jsonify({'error': 'No file uploaded'})
            response.status_code = 400
            return response