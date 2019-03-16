from flask import request, jsonify
import sqlite3


def add_car():
    username = request.json['username']
    car_number = request.json['carNumber']
    db = sqlite3.connect('db.db')
    cur = db.cursor()
    cur.execute('INSERT INTO Cars (username,carNumber,isInside) VALUES (?,?,?)', (username, car_number, 0))
    db.commit()
    db.close()
    return jsonify({'message': 'car added',
                    'status': 'successful',
                    'carNumber': car_number,
                    'username': username})