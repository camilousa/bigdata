from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/', methods=['POST'])
def receive_data():
    sensor = request.form['sensor']
    count = request.form['count']
    print('Recibido ', sensor, count )
    return 'Dato recibido'


app.run()
