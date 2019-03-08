from flask import Flask, request


def get_user():
    app = request.args.get('app')
    return 'amit'
