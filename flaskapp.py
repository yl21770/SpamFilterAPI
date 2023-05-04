from flask import Flask, request
from waitress import serve
import keras

app = Flask(__name__)

model = keras.models.load_model('filtermodel')

@app.route('/predict', methods=['GET'])
def callModel():
	x_value = request.args.get('msg', type=str)
	return str(model.predict([x_value])[0])

if __name__ == '__main__':
	serve(app, host="0.0.0.0", port=8080)