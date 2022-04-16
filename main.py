from flask import Flask

app = Flask(__name__)

@app.route('/learn/<int:id>')
def learn(id):
    return "this is learn: {}".format(str(id))

@app.route('/quiz/<int:id>')
def quiz(id):
    return "this is quiz {}".format(str(id))

@app.route('/quiz_end')
def quiz_end():
    return "Quiz end"

@app.route('/')
def hello():
    return 'Hello, this is home'