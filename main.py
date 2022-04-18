from flask import Flask, render_template, request, jsonify
import os

audio_folder = os.path.join('static', 'audio', 'learn')
print(audio_folder)
#print(os.path.join('static', 'audio', 'learn'))
app = Flask(__name__)
app.config['learn_audio'] = 'static/audio/learn/'

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

    print(id)
    for i in range(5):
        data = learn_data[i]
        print(data)
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
    print(content)

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
            print(answer)
            result = {"correct": "True"}

            if len(answer) != 3:
                result["correct"] = "False"
            else:
                for pair in answer:
                    for i in range(3):
                        solution = quizzes[0]["problem_and_answer"][i]
                        if solution["Romanization"] == pair["Romanization"] and solution["hiragana"] != pair["hiragana"]:
                            print(solution)
                            print(pair)
                            result["correct"] = "False"
                            break
            print(result)
            print(user_result[1])
            return jsonify(newrecord=result)


    return "this is quiz {}".format(str(id))

@app.route('/quiz_end')
def quiz_end():
    return "Quiz end"

@app.route('/')
def hello():
    print(learn_data)
    return render_template('home.html')

if __name__ == '__main__':
   app.run(debug = True)