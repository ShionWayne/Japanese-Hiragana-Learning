from email.mime import audio
import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
audio_folder = os.path.join('static', 'audio')
app.config['learn_audio'] = os.path.join(audio_folder, 'learn')
app.config['quiz_2_audio'] = os.path.join(audio_folder, 'quiz/2')

# learn_dict = {'a': 'あ','i':'い', 'u': 'う', 'e': 'え', 'o':'お'}
learn_data = [
    {
        'id': 'a',
        'hiragana': 'あ',
        'sounds_like': 'ah',
        'audio': os.path.join("../"+app.config['learn_audio'], 'a.mp3')
    },
    {
        'id': 'i',
        'hiragana': 'い',
        'sounds_like': 'e',
        'audio': os.path.join("../"+app.config['learn_audio'], 'i.mp3')
    },
    {
        'id': 'u',
        'hiragana': 'う',
        'sounds_like': 'woo',
        'audio': os.path.join("../"+app.config['learn_audio'], 'u.mp3')
    },
    {
        'id': 'e',
        'hiragana': 'え',
        'sounds_like': 'i',
        'audio': os.path.join("../"+app.config['learn_audio'], 'e.mp3')
    },
    {
        'id': 'o',
        'hiragana': 'お',
        'sounds_like': 'o',
        'audio': os.path.join("../"+app.config['learn_audio'], 'o.mp3')
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

quizzes = [
    {
        "id": 1,
        "type": "drag",
        "problem_text": "Drag the hiragana to corresponding Romanization:",
        "problem_and_answer": [
            {"hiragana": "あい", "Romanization": "uo", "English": "fish"},
            {"hiragana": "うお", "Romanization": "ie", "English": "home"},
            {"hiragana": "いえ", "Romanization": "ai", "English": "love"}
        ]
    }
]

user_result ={
    1: [],
    2: [],
    3: [],
    4: []
}

@app.route('/learn/<id>')
def learn(id):
    for i in range(5):
        data = learn_data[i]
        if data['id'] == id:
            content = data
            break

    if i == 0:
        content['prev'] = 'None'
    else:
        content['prev'] = learn_data[i-1]['id']

    if i == 4:
        content['next'] = 'None'
    else:
        content['next'] = learn_data[i+1]['id']

    return render_template('learn.html', content=content)

@app.route('/quiz/<int:id>', methods=['GET', 'POST'])
def quiz(id):
    if id == 1:
        if request.method == 'GET':
            return render_template("quiz_1.html", content=quizzes[0])
        else:
            json_data = request.get_json()
            user_result[1].append(json_data)
            answer = []
            for element in json_data["user_answer"]:
                if len(element) == 2:
                    answer.append(element)
            result = {"correct": "True"}

            if len(answer) != 3:
                result["correct"] = "False"
            else:
                for pair in answer:
                    for i in range(3):
                        solution = quizzes[0]["problem_and_answer"][i]
                        if solution["Romanization"] == pair["Romanization"] and solution["hiragana"] != pair["hiragana"]:
                            result["correct"] = "False"
                            break
            return jsonify(newrecord=result)
    if id == 2:
        return render_template("quiz_2.html", data=quiz_2_data, p_id=id)
    if id == 3:
        return render_template("quiz_3.html", data=quiz_3_data, p_id=id)
    if id == 4:
        return render_template("quiz_4.html", )
    return "this is quiz {}".format(str(id))


@app.route('/quiz_end')
def quiz_end():
    return render_template('end.html')

@app.route('/')
def hello():
    return render_template('home.html')

if __name__ == '__main__':
   app.run(debug = True)