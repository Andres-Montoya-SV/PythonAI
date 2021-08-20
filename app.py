import pyttsx3
from flask import Flask, request
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')

@app.route('/')
def index():
    return {'response': True, 'msg': 'Hi :)'}

@app.route('/tts', methods=['POST'])
def tts():
    try:
        text = request.json['text']
        ttsEngine = pyttsx3.init()
        ttsEngine.setProperty('rate', 150)
        ttsEngine.say(str(text))
        ttsEngine.runAndWait()
        return f'The app said: {text}', 200
    except:
        raise

if __name__ == '__main__':
    app.run(debug=True, port=8000)