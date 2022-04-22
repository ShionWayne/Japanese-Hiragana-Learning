from email.mime import audio
import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
image_folder = os.path.join('static', 'image')
audio_folder = os.path.join('static', 'audio')
app.config['image_folder'] = image_folder
app.config['learn_audio'] = 'static/audio/learn/'
app.config['quiz_2_audio'] = os.path.join(audio_folder, 'quiz/2')


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

@app.route('/quiz/<int:id>', methods=['GET', 'POST'])
def quiz(id):
    return render_template("quiz_layout.html", q_type=id)
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
    #         if json_data["user_answer"] != quiz_3_data[0]["roman"]:
    #             result["correct"] = "False"
    #         return jsonify(newrecord=result)
    # if id == 4:
    #     return render_template("quiz_4.html", data=quiz_4_data, p_id=id)
    # return "this is quiz {}".format(str(id))


@app.route('/quiz_end')
def quiz_end():
    return render_template('end.html')

@app.route('/')
def hello():
    homeimg = os.path.join(app.config['image_folder'], 'homeimg.png')
    return render_template('home.html', homeimg=homeimg)
    
if __name__ == '__main__':
   app.run(debug = True)
