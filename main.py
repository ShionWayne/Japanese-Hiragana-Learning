import os
import random
from email.mime import audio
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
image_folder = os.path.join('static', 'image')
audio_folder = os.path.join('static', 'audio')
app.config['image_folder'] = image_folder
app.config['learn_audio'] = 'static/audio/learn/'
app.config['quiz_2_audio'] = os.path.join(audio_folder, 'quiz/2')
app.config['quiz_4_audio'] = os.path.join(audio_folder, 'quiz/4')
#------------------------------ data code ------------------------------
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

quiz_1_data = [
    {
        "q_type": 1,
        "type": "drag",
        "problem_text": "Drag the hiragana to corresponding Romanization:",
        "problem_and_answer": [
            {"hiragana": "あい", "Romanization": "ai", "English": "love"},
            {"hiragana": "うお", "Romanization": "uo", "English": "fish"},
            {"hiragana": "いえ", "Romanization": "ie", "English": "home"}
        ]
    }, 
    {
        "q_type": 1,
        "type": "drag",
        "problem_text": "Drag the hiragana to corresponding Romanization:",
        "problem_and_answer": [
            {"hiragana": "うえ", "Romanization": "ue", "English": "hunger"},
            {"hiragana": "おい", "Romanization": "oi", "English": "nephew"},
            {"hiragana": "おう", "Romanization": "ou", "English": "chase"}
        ]
    }
]

quiz_2_data = [
    {
        "q_type": 2,
        "data":[
            {
                "hiragana": "おい",
                "roman": "oi",
                "eng": "hey",
                "audio": os.path.join("../" + app.config['quiz_2_audio'], 'oi.mp3')
            },
            {
                "hiragana": "うえ",
                "roman": "ue",
                "eng": "up",
                "audio": os.path.join("../" + app.config['quiz_2_audio'], 'ue.mp3')
            },
            {
                "hiragana": "あう",
                "roman": "au",
                "eng": "meet",
                "audio": os.path.join("../" + app.config['quiz_2_audio'], 'au.mp3')
            }            
        ]
    },
    {
        "q_type": 2,
        "data":[
            {
                "hiragana": "いい",
                "roman": "ii",
                "eng": "good",
                "audio": os.path.join("../" + app.config['quiz_2_audio'], 'ii.mp3')
            },
            {
                "hiragana": "いう",
                "roman": "iu",
                "eng": "say",
                "audio": os.path.join("../" + app.config['quiz_2_audio'], 'iu.mp3')
            },
            {
                "hiragana": "おう",
                "roman": "ou",
                "eng": "king",
                "audio": os.path.join("../" + app.config['quiz_2_audio'], 'ou.mp3')
            }          
        ]
    }
]

quiz_3_data = [
    {
        "q_type": 3,
        "hiragana": "あおい",
        "roman": "aoi",
        "eng": "blue"
    },
    {
        "q_type": 3,
        "hiragana": "おおう",
        "roman": "oou",
        "eng": "cover"
    },
    {
        "q_type": 3,
        "hiragana": "いいあう",
        "roman": "iiau",
        "eng": "debate"
    }
]

quiz_4_data = [
    {
        "q_type": 4,
        "roman": "iie",
        "eng": "no",
        "audio": os.path.join("../" + app.config['quiz_4_audio'], 'iie.mp3')
    },
    {
        "q_type": 4,
        "roman": "iou",
        "eng": "sulfur",
        "audio": os.path.join("../" + app.config['quiz_4_audio'], 'iou.mp3')
    },
    {
        "q_type": 4,
        "roman": "ooi",
        "eng": "many",
        "audio": os.path.join("../" + app.config['quiz_4_audio'], 'ooi.mp3')
    }
]

#------------------------------ server code ------------------------------

# 
'''
q_num: number of quizzes sampled from the quizzes pool
q_selected_data: quizzes randomly sampled in the size of q_num
user_result: a list of T/F records the validation records
c_num: the total correct number
'''

q_num = 8
q_selected_data = []
user_result = []
c_num = 0
w_num = 0
# use correct dict to record the number of correctly answered quizzes
correct_dict = {}

for i in range(1, q_num + 1):
    correct_dict[i] = 0


def init_data():
    q_1_data = random.sample(quiz_1_data, 1)
    q_2_data = random.sample(quiz_2_data, 1)
    q_data = q_1_data + q_2_data + quiz_3_data + quiz_4_data
    global q_selected_data
    q_selected_data = q_data
    for i in range(q_num):
        q_selected_data[i]["q_id"] = i
    global user_result
    print(q_data)
    user_result = list()

init_data()

@app.route('/startlearning')
def start_learn():
    return render_template('learn_0.html')

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

@app.route('/quiz_valid/<int:id>', methods=['POST'])
def quiz_valid(id):
    cur_data = q_selected_data[id]
    global c_num
    global w_num
    global q_num
    wrong3 = 0
    # write your check code here
    # and validate the c_num via ajax
    json_data = request.get_json()
    user_result.append(json_data)
    if json_data["q_type"] == 1:
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
                    solution = cur_data["problem_and_answer"][i]
                    if solution["Romanization"] == pair["Romanization"] and solution["hiragana"] != pair["hiragana"]:
                        result["correct"] = "False"
                        break
        if result["correct"] == "True":
            correct_dict[1] = 1
        else:
            w_num += 1
        c_num = 0
        for i in range(1, q_num + 1):
            c_num += correct_dict[i]
        if w_num == 3:
            wrong3 = 1
            w_num = 0
        return jsonify(newrecord=result, wrong3=wrong3)

    elif json_data["q_type"] == 2:
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
                    solution = cur_data["data"][i]
                    if solution["roman"] == pair["Romanization"] and solution["hiragana"] != pair["hiragana"]:
                        result["correct"] = "False"
                        break
        if result["correct"] == "True":
            correct_dict[2] = 1
        else: 
            w_num += 1
        c_num = 0
        for i in range(1, q_num + 1):
            c_num += correct_dict[i]
        if w_num == 3:
            wrong3 = 1
            w_num = 0
        return jsonify(newrecord=result, wrong3=wrong3)

    elif json_data["q_type"] == 3:
        if json_data["eng"] == "blue":
            if json_data["user_answer"] == "aoi":
                result = {"correct": "True"}
                correct_dict[3] = 1
            else:
                result = {"correct": "False"}
                w_num += 1
        if json_data["eng"] == "cover":
            if json_data["user_answer"] == "oou":
                result = {"correct": "True"}
                correct_dict[4] = 1
            else:
                result = {"correct": "False"}
                w_num += 1
        if json_data["eng"] == "debate":
            if json_data["user_answer"] == "iiau":
                result = {"correct": "True"}
                correct_dict[5] = 1
            else:
                result = {"correct": "False"}
                w_num += 1
        c_num = 0
        for i in range(1, q_num + 1):
            c_num += correct_dict[i]
        if w_num == 3:
            wrong3 = 1
            w_num = 0
        return jsonify(newrecord=result, wrong3=wrong3)

    elif json_data["q_type"] == 4:
        if json_data["eng"] == "no":
            if json_data["user_answer"] == "iie":
                result = {"correct": "True"}
                correct_dict[6] = 1
            else:
                result = {"correct": "False"}
                w_num += 1
        if json_data["eng"] == "sulfur":
            if json_data["user_answer"] == "iou":
                result = {"correct": "True"}
                correct_dict[7] = 1
            else:
                result = {"correct": "False"}
                w_num += 1
        if json_data["eng"] == "many":
            if json_data["user_answer"] == "ooi":
                result = {"correct": "True"}
                correct_dict[8] = 1
            else:
                result = {"correct": "False"}
                w_num += 1
        c_num = 0
        for i in range(1, q_num + 1):
            c_num += correct_dict[i]
        if w_num == 3:
            wrong3 = 1
            w_num = 0
        return jsonify(newrecord=result, wrong3=wrong3)


@app.route('/quiz/<int:id>')
def quiz(id):
    # global w_num
    if id > q_num:
        return "error: no id found"
    cur_q = q_selected_data[id]
    # wrong3 = 0
    # if w_num == 3:
    #     wrong3 = 1
    #     w_num = 0
    return render_template("quiz_arch.html", data=cur_q, p_id=id, q_num=q_num, c_num=c_num)

    
    # if id == 1:
    #     if request.method == 'GET':
    #         return render_template("quiz_1.html", content=quizzes[0])
    #     else:
    #         json_data = request.get_json()
    #         user_result[1].append(json_data)
    #         answer = []
    #         for element in json_data["user_answer"]:
    #             if len(element) == 2:
    #                 answer.append(element)
    #         result = {"correct": "True"}

    #         if len(answer) != 3:
    #             result["correct"] = "False"
    #         else:
    #             for pair in answer:
    #                 for i in range(3):
    #                     solution = quizzes[0]["problem_and_answer"][i]
    #                     if solution["Romanization"] == pair["Romanization"] and solution["hiragana"] != pair["hiragana"]:
    #                         result["correct"] = "False"
    #                         break
    #         return jsonify(newrecord=result)
    # if id == 2:
    #     return render_template("quiz_2.html", data=quiz_2_data, p_id=id)
    # if id == 3:
    #     if request.method == 'GET':
    #         return render_template("quiz_3.html", data=quiz_3_data, p_id=id)
    #     else:
    #         json_data = request.get_json()
    #         user_result[3].append(json_data)
    #         result = {"correct": "True"}
    #         if json_data["user_answer"] != quiz_3_data[0]["eng"]:
    #             result["correct"] = "False"
    #         return jsonify(newrecord=result)
    # if id == 4:
    #     return render_template("quiz_4.html", data=quiz_4_data, p_id=id)
    # return "this is quiz {}".format(str(id))


@app.route('/quiz_end')
def quiz_end():
    return render_template('end.html', q_num=q_num, c_num=c_num)

@app.route('/')
def hello():
    homeimg = os.path.join(app.config['image_folder'], 'homeimg.png')
    return render_template('home.html', homeimg=homeimg)

if __name__ == '__main__':
    app.run(debug = True)