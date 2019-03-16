from flask import request, jsonify
import sqlite3


def get_all_user_cars():
    username = request.args.get('username')
    db = sqlite3.connect('db.db')
    cur = db.cursor()
    cur.execute('SELECT * FROM Cars WHERE username = ?', (username,))
    cars_list = cur.fetchall()
    status = 'authorized' if cars_list is not None else 'unauthorized'
    db.close()
    return jsonify({"data": cars_list, "status": status})
