from flask import Flask, request, jsonify

import pickle
import numpy as np
import pandas as pd
import json

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add():
    num = request.json.get('num')
    if num > 10:
        return 'too much', 400
    return jsonify({
        'result': num + 1
    })


with open('web/dp_model.pkl', 'rb') as pkl_file:
    model = pickle.load(pkl_file)

@app.route('/predict', methods=['POST'])
def predict_func():
	features = request.json
	cols = ['status', 'propertyType', 'baths', 'beds', 'sqft', 'state', 'Period built']
	features_f = pd.DataFrame([features], columns=cols)
	predict = model.predict(features_f)
	return jsonify({'prediction': round(predict[0])})


if __name__ == '__main__':

    app.run('localhost', 5000)