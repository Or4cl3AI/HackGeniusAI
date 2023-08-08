```python
import os
from flask import Flask, request, jsonify
from flask_socketio import SocketIO, join_room, leave_room, send

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

user_progress = {}
user_profile = {}
study_groups = {}

@app.route('/join_study_group', methods=['POST'])
def join_study_group():
    data = request.get_json()
    user_id = data['user_id']
    group_id = data['group_id']

    if group_id not in study_groups:
        study_groups[group_id] = []

    study_groups[group_id].append(user_id)
    return jsonify({"message": "Successfully joined the study group"}), 200

@socketio.on('send_message')
def handle_send_message_event(data):
    app.logger.info("{} has sent message to the room {}: {}".format(data['username'], data['room'], data['message']))
    socketio.emit('receive_message', data, room=data['room'])

@socketio.on('join_room')
def handle_join_room_event(data):
    app.logger.info("{} has joined the room {}".format(data['username'], data['room']))
    join_room(data['room'])
    socketio.emit('join_room_announcement', data, room=data['room'])

@socketio.on('leave_room')
def handle_leave_room_event(data):
    app.logger.info("{} has left the room {}".format(data['username'], data['room']))
    leave_room(data['room'])
    socketio.emit('leave_room_announcement', data, room=data['room'])

if __name__ == '__main__':
    socketio.run(app, debug=True)
```