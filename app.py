from flask import Flask
from flask_cors import CORS
from api.login import login
from api.get_all_user_cars import get_all_user_cars
from api.add_car import add_car

app = Flask(__name__)
CORS(app)


@app.route('/login', methods=['POST'])
def login_route():
    return login()


@app.route('/get_all_user_cars', methods=['GET'])
def get_all_user_cars_route():
    return get_all_user_cars()


@app.route('/add_car', methods=['POST'])
def add_car_route():
    return add_car()


if __name__ == '__main__':
    app.run(debug=True)
