from flask import Flask
from flask import render_template, redirect
from flask import Response, request, jsonify
app = Flask(__name__)

# ROUTES
@app.route('/')
def index():
    return redirect('home')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/letters')
def letters():
    return render_template('letters/letters.html')

@app.route('/words')
def words():
    return render_template('words/words.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz/quiz.html')

if __name__ == '__main__':
   app.run(debug = True)