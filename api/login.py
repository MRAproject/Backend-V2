from flask import request
import sqlite3


def login():
    username = request.json['username']
    password = request.json['password']
    conn = sqlite3.connect('db.db')
    conn.execute(
        'CREATE TABLE Users (username TEXT PRIMARY KEY, password TEXT, firstName TEXT, lastName TEXT, capacity INTEGER)')
    print("Table created successfully")
    conn.close()
    return 'enter'
