from email.mime import audio
import os
from flask import Flask, render_template
import os


image_folder = os.path.join('static', 'image')
audio_folder = os.path.join('static', 'audio')

app = Flask(__name__)
app.config['image_folder'] = image_folder
app.config['learn_audio'] = os.path.join(audio_folder, 'learn')
app.config['quiz_2_audio'] = os.path.join(audio_folder, 'quiz/2')

learn_dict = {'a': 'あ','i':'い', 'u': 'う', 'e': 'え', 'o':'お'}
learn_data = [
    {
        'id': 'a',
        'hiragana': 'あ',
        'sounds_like': 'ah',
        'audio': os.path.join(app.config['learn_audio'], 'a.mp3')
    },
    {
        'id': 'i',
        'hiragana': 'い',
        'sounds_like': 'e',
        'audio': os.path.join(app.config['learn_audio'], 'i.mp3')
    },
    {
        'id': 'u',
        'hiragana': 'う',
        'sounds_like': 'woo',
        'audio': os.path.join(app.config['learn_audio'], 'u.mp3')
    },
    {
        'id': 'e',
        'hiragana': 'え',
        'sounds_like': 'i',
        'audio': os.path.join(app.config['learn_audio'], 'e.mp3')
    },
    {
        'id': 'o',
        'hiragana': 'お',
        'sounds_like': 'o',
        'audio': os.path.join(app.config['learn_audio'], 'o.mp3')
    }
]

quiz_2_data = [
    {
        "q_type": 2,
        "hiragana": "おい",
        "roman": "hey",
        "audio": os.path.join("../" + app.config['quiz_2_audio'], 'oi.mp3')
    },
    {
        "q_type": 2,
        "hiragana": "うえ",
        "roman": "up",
        "audio": os.path.join("../" + app.config['quiz_2_audio'], 'ue.mp3')
    },
    {
        "q_type": 2,
        "hiragana": "あう",
        "roman": "Meet",
        "audio": os.path.join("../" + app.config['quiz_2_audio'], 'au.mp3')
    }
]


quiz_3_data = [
    {
        "q_type": 3,
        "hiragana": "あおい",
        "roman": "blue"
    }
]

@app.route('/startlearning')
def start_learn():
    return render_template('learn_0.html')

@app.route('/learn/<int:id>')
def learn(id):
    return "this is learn: {}".format(str(id))

@app.route('/quiz/<int:id>')
def quiz(id):
    if id == 2:
        return render_template("quiz_2.html", data=quiz_2_data, p_id=id)
    if id == 3:
        return render_template("quiz_3.html", data=quiz_3_data, p_id=id)
    return "this is quiz {}".format(str(id))

@app.route('/quiz_end')
def quiz_end():
    return "Quiz end"

@app.route('/')
def hello():
    print(learn_dict)
    homeimg = os.path.join(app.config['image_folder'], 'homeimg.png')
    return render_template('home.html', homeimg=homeimg)

if __name__ == '__main__':
   app.run(debug = True)