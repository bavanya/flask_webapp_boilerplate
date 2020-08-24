import flask
from flask import request,render_template
from flask_socketio import SocketIO

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'littledidiknow@007'

socketio = SocketIO(app)

@app.route('/')
def home():
    return "hi"

def successConnection(methods=['GET', 'POST']):
    print('the message transfer is a success')


@socketio.on('event by client')
def connect(json, methods=['GET', 'POST']):
    print('the received data is ' + str(json))
    socketio.emit('the response is', json, callback=successConnection)

if __name__ == '__main__':
    socketio.run(app, debug=True)

