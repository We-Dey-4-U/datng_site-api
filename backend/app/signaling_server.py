# app/signaling_server.py
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('offer')
def handle_offer(data):
    # Handle video call offer
    emit('offer', data, broadcast=True)

@socketio.on('answer')
def handle_answer(data):
    # Handle video call answer
    emit('answer', data, broadcast=True)

@socketio.on('ice_candidate')
def handle_ice_candidate(data):
    # Handle ICE candidate exchange
    emit('ice_candidate', data, broadcast=True)

@socketio.on('private_message')
def handle_private_message(data):
    # Handle private text message
    emit('private_message', data, room=data['receiver_id'])

if __name__ == '__main__':
    socketio.run(app, debug=True)