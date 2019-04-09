from flask import request, jsonify
import sqlite3


def add_car():
    username = request.json['username']
    car_number = request.json['carNumber']
    db = sqlite3.connect('db.db')
    cur = db.cursor()
    try:
        cur.execute('INSERT INTO Cars (username,carNumber,isInside) VALUES (?,?,?)', (username, car_number, 0))
        db.commit()
    except Exception as e:
        print(e)
        return jsonify({'message': f'Car number {car_number} is alreday exist',
                        'status': 'failed'})
    finally:
        db.close()
    return jsonify({'message': 'car added',
                    'status': 'successful',
                    'carNumber': car_number,
                    'username': username})
