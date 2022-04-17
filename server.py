from flask import Flask
from flask import render_template, redirect
from flask import Response, request, jsonify
app = Flask(__name__)

learning_char = {
    "A": {
        "id": 1,
        "morse_code": ".-",
        "quick_memory_image": "static/quick_memory_image/Morse-Code-Letter-A.jpg",
        "morse_code_sounds": "static/morse_code_sounds/mcs-a.wav",
        "previous": "/letters",
        "next": "/letters/C"
    },
    "C": {
        "id": 2,
        "morse_code": "-.-.",
        "quick_memory_image": "static/quick_memory_image/Morse-Code-Letter-C.jpg",
        "morse_code_sounds": "static/morse_code_sounds/mcs-c.wav",
        "previous": "/letters/A",
        "next": "/letters/E"
    },
    "E": {
        "id": 3,
        "morse_code": ".",
        "quick_memory_image": "static/quick_memory_image/Morse-Code-Letter-E.jpg",
        "morse_code_sounds": "static/morse_code_sounds/mcs-e.wav",
        "previous": "/letters/C",
        "next": "/letters/H"
    },
    "H": {
        "id": 4,
        "morse_code": "....",
        "quick_memory_image": "static/quick_memory_image/Morse-Code-Letter-H.jpg",
        "morse_code_sounds": "static/morse_code_sounds/mcs-h.wav",
        "previous": "/letters/E",
        "next": "/letters/L"
    },
    "L": {
        "id": 5,
        "morse_code": ".-..",
        "quick_memory_image": "static/quick_memory_image/Morse-Code-Letter-L.jpg",
        "morse_code_sounds": "static/morse_code_sounds/mcs-l.wav",
        "previous": "/letters/H",
        "next": "/letters/M"
    },
    "M": {
        "id": 6,
        "morse_code": "--",
        "quick_memory_image": "static/quick_memory_image/Morse-Code-Letter-M.jpg",
        "morse_code_sounds": "static/morse_code_sounds/mcs-m.wav",
        "previous": "/letters/L",
        "next": "/letters/O"
    },
    "O": {
        "id": 7,
        "morse_code": "---",
        "quick_memory_image": "static/quick_memory_image/Morse-Code-Letter-O.jpg",
        "morse_code_sounds": "static/morse_code_sounds/mcs-o.wav",
        "previous": "/letters/M",
        "next": "/letters/P"
    },
    "P": {
        "id": 8,
        "morse_code": ".--.",
        "quick_memory_image": "static/quick_memory_image/Morse-Code-Letter-P.jpg",
        "morse_code_sounds": "static/morse_code_sounds/mcs-p.wav",
        "previous": "/letters/O",
        "next": "/letters/R"
    },
    "R": {
        "id": 9,
        "morse_code": ".-.",
        "quick_memory_image": "static/quick_memory_image/Morse-Code-Letter-R.jpg",
        "morse_code_sounds": "static/morse_code_sounds/mcs-r.wav",
        "previous": "/letters/P",
        "next": "/letters/S"
    },
    "S": {
        "id": 10,
        "morse_code": "...",
        "quick_memory_image": "static/quick_memory_image/Morse-Code-Letter-A.jpg",
        "morse_code_sounds": "static/morse_code_sounds/mcs-a.wav",
        "previous": "/letters/R",
        "next": "/words/HOPE"
    }
}

learning_word = {

    "HOPE": {
        "id": 11,
        "morse_code": [learning_char[c]["morse_code"] for c in "HOPE"],
        "quick_memory_image": [learning_char[c]["quick_memory_image"] for c in "HOPE"],
        "morse_code_sounds": "static/morse_code_sounds/mcs-hope.wav",
        "previous": "/letters/S",
        "next": "/words/PEACE"
    },
    "PEACE": {
        "id": 12,
        "morse_code": [learning_char[c]["morse_code"] for c in "PEACE"],
        "quick_memory_image": [learning_char[c]["quick_memory_image"] for c in "PEACE"],
        "morse_code_sounds": "static/morse_code_sounds/mcs-peace.wav",
        "previous": "/words/HOPE",
        "next": "/quiz"
    },
}
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

@app.route('/letters/<var>')
def show_letters(var=None):
    data = learning_char[var]
    return render_template('letters/letters.html', data=data)

@app.route('/words/<var>')
def words(var=None):
    data = learning_word[var]
    return render_template('words/words.html', data=data)

@app.route('/quiz')
def quiz():
    return render_template('quiz/quiz.html')

if __name__ == '__main__':
   app.run(debug = True)