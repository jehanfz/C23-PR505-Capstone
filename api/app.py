from flask import Flask, request
from flask_restful import Resource, Api
from flask_mysqldb import MySQL

app = Flask(__name__)
api = Api(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'batik'
 
mysql = MySQL(app)

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

class RegisterResource(Resource):
    def get(self):
        pass

    def post(self):
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
 
        with app.app_context():
            cursor = mysql.connection.cursor()
            cursor.execute("""SELECT * FROM register WHERE email=%s""", (email, ))
            user = cursor.fetchall()
            if not user:
                cursor.execute(''' INSERT INTO register VALUES(NULL, %s, %s, %s)''', (username, email, password))
                mysql.connection.commit()
            cursor.close()
        return {'username': username, 'email': email}
    
class LoginResource(Resource):
    def get(self):
        pass
    
    def post(self):
        email = request.form['email']
        password = request.form['password']
 
        with app.app_context():
            cursor = mysql.connection.cursor()
            cursor.execute("""SELECT * FROM login WHERE email=%s""", (email, ))
            user = cursor.fetchall()
            if not user:
                cursor.execute(''' INSERT INTO login VALUES(NULL, %s, %s)''', (email, password))
                mysql.connection.commit()
            cursor.close()
        return {'email': email}


api.add_resource(HelloWorld, '/')
api.add_resource(RegisterResource, '/register')
api.add_resource(LoginResource, '/login')

if __name__ == '__main__':
    app.run(debug=True)

