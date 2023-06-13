from flask_restful import Api

from models import app
from resources.login import LoginResource
from resources.register import RegisterResource
from resources.prediksi_resource import PrediksiResource

api = Api(app)

api.add_resource(LoginResource, '/login')
api.add_resource(RegisterResource, '/register')
api.add_resource(PrediksiResource, '/prediksi')

if __name__ == '__main__':
    app.run(debug=True)

