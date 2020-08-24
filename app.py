import flask
from flask import request,render_template
from flask_socketio import SocketIO

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'littledidiknow@007'

socketio = SocketIO(app)

@app.route('/')
def home():
    return "hi"

if __name__ == '__main__':
    socketio.run(app, debug=True)

