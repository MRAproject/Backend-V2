from flask import request, jsonify
import sqlite3


def get_times():
    username = request.args.get('username')
    db = sqlite3.connect('db.db')
    cur = db.cursor()
    cur.execute('SELECT * FROM times WHERE username = ?', (username,))
    times_list = cur.fetchall()
    status = 'authorized' if times_list is not None else 'unauthorized'
    db.close()
    return jsonify({"data": times_list, "status": status})
