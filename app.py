from flask import Flask, request
from flask_cors import CORS
from api.get_user import get_user

app = Flask(__name__)
CORS(app)


@app.route('/amit', methods=['GET'])
def amit():
    return get_user()


if __name__ == '__main__':
    app.run(debug=True)
