#!/usr/bin/env python
"""server.py

This is the request handler that implements the endpoints"""
import json
import uuid
from flask import Flask, abort, request
import time

MESSAGES = []  # We'll just use a global list until we run out of memory
app = Flask(__name__)


def add_or_update_message():
    """Add a message to the system or update it if a message id is specified"""
    message = request.get_json()
    # TODO: Check to see if we got a message_id in the request, if so update message
    timestamp = time.time()
    message_id = str(uuid.uuid4())
    message['message_id'] = message_id
    message['timestamp'] = timestamp
    MESSAGES.append(message)
    response = {'message_id': message_id}
    return json.dumps(response)


def get_messages():
    """Get all the messages nearby"""
    # TODO: Filter by location
    return json.dumps(MESSAGES)


def remove_message():
    """Remove a message"""
    data = request.get_json()
    message_id = data['message_id']
    for idx, message in enumerate(MESSAGES):
        if message['message_id'] == message_id:
            MESSAGES.pop(idx)
            return ''
    abort(400)


@app.route('/messages', methods=['GET', 'POST', 'DELETE'])
def handle_request():
    if request.method == 'POST':
        return add_or_update_message()
    elif request.method == 'GET':
        return get_messages()
    elif request.method == 'DELETE':
        return remove_message()
    else:
        abort(400)


if __name__ == '__main__':
    app.run()
