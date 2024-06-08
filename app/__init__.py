from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hedgefund.db'
db = SQLAlchemy(app)
CORS(app)
socketio = SocketIO(app)

from app import routes, models, chatbot, ml_model
