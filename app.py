from flask import Flask
from flask_cors import CORS
from api.login import login
from api.get_all_user_cars import get_all_user_cars
from api.add_car import add_car
from api.remove_car import remove_car
from api.edit_user import edit_user
from api.check_car import check_car

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


@app.route('/remove_car', methods=['POST'])
def remove_car_route():
    return remove_car()


@app.route('/edit_user', methods=['POST'])
def edit_user_route():
    return edit_user()


@app.route('/check_car', methods=['GET'])
def check_car_route():
    return check_car()


if __name__ == '__main__':
    app.run(debug=True)
