from flask import Flask, render_template
import os

audio_folder = os.path.join('static', 'audio')

app = Flask(__name__)
app.config['learn_audio'] = os.path.join(audio_folder, 'learn')

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

@app.route('/learn/<int:id>')
def learn(id):
    return "this is learn: {}".format(str(id))

@app.route('/quiz/<int:id>')
def quiz(id):
    if id == 2:
        return render_template("quiz_2.html")
    if id == 4:
        return render_template("quiz_4.html", )
    return "this is quiz {}".format(str(id))

@app.route('/quiz_end')
def quiz_end():
    return render_template('end.html')

@app.route('/')
def hello():
    print(learn_dict)
    return render_template('home.html')

if __name__ == '__main__':
   app.run(debug = True)