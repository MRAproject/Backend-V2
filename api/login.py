from flask import request, jsonify
import sqlite3


def login():
    username = request.json['username']
    password = request.json['password']
    db = sqlite3.connect('db.db')
    cur = db.cursor()
    cur_vars = (username, password)
    cur.execute('SELECT * FROM Users WHERE username=? AND password=?', cur_vars)
    user = cur.fetchone()
    status = 'authorized' if user is not None else 'unauthorized'
    db.close()
    return jsonify({"body": request.json, "status": status})

# cur.execute("INSERT INTO Users (username,password,firstName,lastName,capacity) VALUES(?, ?, ?, ?,?)",
#            ('amitmarko', '12345', 'amit', 'markovich', 100))
# db.commit()
# db.execute(
#  'CREATE TABLE Times (username TEXT, carNumber TEXT, enter TEXT, exit TEXT)')
# print("Table created successfully")
