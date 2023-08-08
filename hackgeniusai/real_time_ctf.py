```python
import random
from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit
from .ai_vulnerability_detection import detect_vulnerability
from .dynamic_learning_path import update_learning_path

app = Flask(__name__)
socketio = SocketIO(app)

challenge_status = {}
user_progress = {}

@app.route('/start_ctf_challenge', methods=['POST'])
def start_ctf_challenge():
    user_id = request.json.get('user_id')
    challenge_id = random.randint(1, 100)  # Randomly select a challenge
    challenge_status[challenge_id] = 'in-progress'
    user_progress[user_id] = challenge_id
    return jsonify({'challenge_id': challenge_id})

@socketio.on('submit_solution')
def handle_solution(data):
    user_id = data.get('user_id')
    challenge_id = user_progress.get(user_id)
    solution = data.get('solution')
    vulnerabilities = detect_vulnerability(solution)
    if vulnerabilities:
        emit('solution_feedback', {'status': 'failed', 'vulnerabilities': vulnerabilities})
    else:
        challenge_status[challenge_id] = 'completed'
        emit('solution_feedback', {'status': 'passed'})
        update_learning_path(user_id, challenge_id)

if __name__ == '__main__':
    socketio.run(app)
```