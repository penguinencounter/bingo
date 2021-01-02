from flask import Flask, render_template, request, redirect
import random

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def root():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        formdata = request.form
        if formdata["set_id"]:
            print('ok')
            return redirect(f'/{formdata["set_id"]}/')
        else:
            return render_template('index.html')


@app.route('/word/')
def word():
    with open('bingo_words.txt') as f:
        return random.choice(f.read().split('\n'))


@app.route('/<set_id>/')
def application(set_id):
    return render_template('bingo.html')


app.run(debug=True, host='0.0.0.0')
