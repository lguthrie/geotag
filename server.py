#!/usr/bin/env python
"""server.py

This is the request handler that implements the endpoints"""
from flask import Flask, abort

app = Flask(__name__)


def add_message():
    """Add a message to the system"""
    raise NotImplemented


def get_messages():
    """Get all the messages nearby"""
    raise NotImplemented


def remove_message():
    """Remove a message"""
    raise NotImplemented


# noinspection PyUnresolvedReferences
@app.route('/messages')
def handle_request():
    if request.method == 'POST':
        add_message()
    elif request.method == 'GET':
        get_messages()
    elif request.method == 'DELETE':
        remove_message()
    else:
        abort(400)


if __name__ == '__main__':
    app.run()
