from flask import Flask, request, jsonify
from flask_cors import CORS
import util

app = Flask(__name__)

# Allow cross-origin requests during local development
CORS(app)


@app.route("/api/hello")
def hello():
    return "Hello World"


@app.route("/api/get_location_names")
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    #response = util.get_location_names()
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route("/api/predict_home_price", methods=['GET', 'POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])
    response = jsonify({
        "estimated_price": util.get_estimated_price(location,total_sqft,bhk,bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    # response = util.get_estimated_price('1st Phase JP Nagar', 1000, 3, 3)
    return response


if __name__ == '__main__':
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    #app.run(host='127.0.0.1', port=5000, debug=True)
    app.run(host='127.0.0.1', port=5000)
