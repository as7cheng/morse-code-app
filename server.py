from flask import Flask
from flask import render_template, redirect
from flask import Response, request, jsonify
app = Flask(__name__)

data = [
    {
        "id": 1,
        "letter": "A",
        "img_le": "../static/assert/letter_image/LETTER_A_LIFT.png",
        "img_ri": "../static/assert/quick_memory_image/Morse-Code-Letter-A.jpg",
        "sound": "../static/assert/morse_code_sounds/mcs-a.wav"
    },
    {
        "id": 2,
        "letter": "C",
        "img_le": "../static/assert/letter_image/LETTER_C_LIFT.png",
        "img_ri": "../static/assert/quick_memory_image/Morse-Code-Letter-C.jpg",
        "sound": "../static/assert/morse_code_sounds/mcs-c.wav"
    },
    {
        "id": 3,
        "letter": "E",
        "img_le": "../static/assert/letter_image/LETTER_E_LIFT.png",
        "img_ri": "../static/assert/quick_memory_image/Morse-Code-Letter-E.jpg",
        "sound": "../static/assert/morse_code_sounds/mcs-e.wav"
    },
    {
        "id": 4,
        "letter": "H",
        "img_le": "../static/assert/letter_image/LETTER_H_LIFT.png",
        "img_ri": "../static/assert/quick_memory_image/Morse-Code-Letter-H.jpg",
        "sound": "../static/assert/morse_code_sounds/mcs-h.wav"
    },
    {
        "id": 5,
        "letter": "L",
        "img_le": "../static/assert/letter_image/LETTER_L_LIFT.png",
        "img_ri": "../static/assert/quick_memory_image/Morse-Code-Letter-L.jpg",
        "sound": "../static/assert/morse_code_sounds/mcs-l.wav"
    },
    {
        "id": 6,
        "letter": "M",
        "img_le": "../static/assert/letter_image/LETTER_M_LIFT.png",
        "img_ri": "../static/assert/quick_memory_image/Morse-Code-Letter-M.jpg",
        "sound": "../static/assert/morse_code_sounds/mcs-m.wav"
    },
    {
        "id": 7,
        "letter": "O",
        "img_le": "../static/assert/letter_image/LETTER_O_LIFT.png",
        "img_ri": "../static/assert/quick_memory_image/Morse-Code-Letter-O.jpg",
        "sound": "../static/assert/morse_code_sounds/mcs-o.wav"
    },
    {
        "id": 8,
        "letter": "P",
        "img_le": "../static/assert/letter_image/LETTER_P_LIFT.png",
        "img_ri": "../static/assert/quick_memory_image/Morse-Code-Letter-P.jpg",
        "sound": "../static/assert/morse_code_sounds/mcs-p.wav"
    },
    {
        "id": 9,
        "letter": "R",
        "img_le": "../static/assert/letter_image/LETTER_R_LIFT.png",
        "img_ri": "../static/assert/quick_memory_image/Morse-Code-Letter-R.jpg",
        "sound": "../static/assert/morse_code_sounds/mcs-r.wav"
    },
    {
        "id": 10,
        "letter": "S",
        "img_le": "../static/assert/letter_image/LETTER_S_LIFT.png",
        "img_ri": "../static/assert/quick_memory_image/Morse-Code-Letter-S.jpg",
        "sound": "../static/assert/morse_code_sounds/mcs-s.wav"
    },
]


# ROUTES
@app.route('/')
def index():
    return redirect('home')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/letters/0')
def letters():
    return render_template('letters/letters.html')

@app.route('/letters/<id>')
def letters_letter(id=1):
    global data
    for letter in data:
        if letter["id"] == int(id):
            return render_template('letters/letters_letter.html', data=data, letter=letter)

@app.route('/words/1')
def words():
    return render_template('words/words_1.html')

@app.route('/words/2')
def words_2():
    return render_template('words/words_2.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz/quiz.html')

@app.route('/quiz/<num>')
def quiz_questions(num):
    data = 'quizData'
    return render_template('quiz/quiz' + num + '.html', data = data)

@app.route('/quiz/<num>/result', methods=["POST", "GET"])
def quiz_questions_result(num):
    data = {
        "result": 0,
        "selected": 'A',
        "rightAwswer": 'E'
    }
    return render_template('quiz/quiz' + num + 'Result.html', data = data)

if __name__ == '__main__':
   app.run(debug = True)