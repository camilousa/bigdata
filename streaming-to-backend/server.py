from flask import Flask
from flask import request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

data = {}
@app.route('/', methods=['POST'])
def receive_data():
    sensor = request.form['sensor']
    count = request.form['count']
    print('Recibido ', sensor, count )
    data[sensor] = count
    return 'Dato recibido'

@app.route('/dashboard')
def dashboard():
    return  data

app.run()
