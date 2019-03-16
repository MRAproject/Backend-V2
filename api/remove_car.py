from flask import request, jsonify
import sqlite3


def remove_car():
    username = request.json['username']
    car_number = request.json['carNumber']
    db = sqlite3.connect('db.db')
    cur = db.cursor()
    cur.execute('DELETE FROM Cars WHERE username = ? AND carNumber= ?', (username, car_number))
    db.commit()
    db.close()
    return jsonify({'message': 'car deleted',
                    'status': 'successful',
                    'carNumber': car_number,
                    'username': username})
