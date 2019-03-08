from flask import Flask
from flask_cors import CORS
from api.login import login

app = Flask(__name__)
CORS(app)


@app.route('/login', methods=['POST'])
def login_route():
    return login()


if __name__ == '__main__':
    app.run(debug=True)
