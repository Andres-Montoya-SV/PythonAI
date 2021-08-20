from flask import Flask, request, send_file
import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from gtts import gTTS
import uuid

load_dotenv()
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
db = SQLAlchemy(app)

class Usermessages(db.Model):
    _id = db.Column('id', db.Integer, primary_key=True)
    _messages = db.Column(db.String(10000))

    def __init__(self, _messages):
        self._messages = _messages

@app.route('/')
def index():
    return {'response': True, 'msg': 'Hi :)'}

@app.route('/tts', methods=['POST'])
def tts():
    try:
        text = request.json['text']
        user = Usermessages(_messages=text)
        db.session.add(user)
        db.session.commit()
        tts = gTTS(text)
        uuidOne = uuid.uuid1()
        downloadfile = f'{uuidOne}.mp3'
        tts.save(f"{downloadfile}")
        os.system(f"start {downloadfile}")
        return send_file(f"{downloadfile}"), 200
    except:
        raise

@app.route('/chatbot', methods=['POST'])
def chatbot():
    try:
        return 'works'
    except:
        raise

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=8000)