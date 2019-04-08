from flask import request, jsonify
from datetime import datetime
import sqlite3
import base64
from plate_recognition.Main import main


def check_car():
    image = request.args.get('carNumber')
    img_data = base64.b64decode(str(image))

    filename = 'some_image.jpg'  # I assume you have a way of picking unique filenames
    with open(filename, 'wb') as f:
        f.write(img_data)

    try:
        car_number = main(img_data)
        print(f'car number {car_number}')
        if car_number is None:
            return jsonify({'message': 'car number is alreday exist',
                            'status': 'failed'})
        db = sqlite3.connect('db.db')
        cur = db.cursor()
        cur.execute('SELECT * FROM Cars WHERE carNumber = ?', (car_number,))
        car = cur.fetchone()
    except Exception as e:
        print(e)
        return jsonify({'message': 'car number is alreday exist',
                        'status': 'failed'})
    if car is None:
        db.close()
        return jsonify({"state": 'authorized'})
    date = datetime.now().strftime("%d/%m/%y, %H:%M")
    username = car[0]
    # find last action
    cur.execute('SELECT * FROM Times WHERE carNumber = ? AND username = ? ', (car_number, username))
    car_time = cur.fetchall()
    last_action = car_time[len(car_time) - 1]
    time_enter = last_action[2] if last_action[3] is None else last_action[3]
    ans = datetime.now() - datetime.strptime(time_enter, "%d/%m/%y, %H:%M")
    if ans.seconds <= 60:
        print('car need to wait')
        return jsonify({'message': 'car number is alreday exist',
                        'status': 'failed'})
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
