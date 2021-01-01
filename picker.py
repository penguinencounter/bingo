from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def root():
    return 'test'

app.run(debug=True, host='0.0.0.0')
