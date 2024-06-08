from flask import request, jsonify, render_template
from app import app, db
from app.models import User, Chat
from app.chatbot import get_bot_response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_id = data['user_id']
    message = data['message']
    
    response = get_bot_response(message)
    
    new_chat = Chat(user_id=user_id, message=message, response=response)
    db.session.add(new_chat)
    db.session.commit()
    
    return jsonify({'response': response})
