from flask import request, jsonify
import sqlite3


def edit_user():
    username = request.json['username']
    first_name = request.json['firstName']
    last_name = request.json['lastName']
    password = request.json['password']
    capacity = request.json['capacity']
    db = sqlite3.connect('db.db')
    cur = db.cursor()
    cur.execute('UPDATE Users SET password = ?, firstName = ?, lastName = ?, capacity = ? WHERE username = ?',
                (password, first_name, last_name, capacity, username))
    db.commit()
    db.close()
    return jsonify({"message": "edit user", "status": "successful", "data": request.json})
