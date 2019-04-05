from flask import request, jsonify
from datetime import datetime
import sqlite3
import base64


def check_car():
    image = request.args.get('carNumber')
    img_data = base64.b64decode(str(image))

    db = sqlite3.connect('db.db')
    cur = db.cursor()
    cur.execute('SELECT * FROM Cars WHERE carNumber = ?', (car_number,))
    car = cur.fetchone()
    if car is None:
        db.close()
        return jsonify({"state": 'authorized'})
    date = datetime.now().strftime("%d/%m/%y, %H:%M")
    username = car[0]
    if car[2] == 0:
        # enter to parking
        cur.execute('INSERT INTO Times (username,carNumber,enter,exit) VALUES (?,?,?,?)',
                    (username, car_number, date, None))
        cur.execute('UPDATE Cars SET isInside = ? WHERE carNumber = ? AND username = ?', (1, car_number, username))
    else:
        # exist from parking
        cur.execute('SELECT * FROM Times WHERE carNumber = ? AND username = ? AND exit IS NULL', (car_number, username))
        car_time = cur.fetchone()
        cur.execute('UPDATE Times SET exit = ? WHERE username = ? AND carNumber = ? AND enter = ?',
                    (date, username, car_number, car_time[2]))
        cur.execute('UPDATE Cars SET isInside = ? WHERE carNumber = ? AND username = ?',
                    (0, car_number, username))
    db.commit()
    db.close()
    return jsonify({"status": 'done'})
