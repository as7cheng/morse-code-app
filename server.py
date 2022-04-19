from flask import Flask
from flask import render_template, redirect
from flask import Response, request, jsonify
from datetime import datetime
app = Flask(__name__)

learning_data = [
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

quiz_data = [
    {
        "id": 1,
        "type": "selection",
        "img": "../static/assert/quiz/quiz_images/quiz01Question.png",
        "img2": "",
        "questionName": "Select the right answer:",
        "placeholder": "",
        "audio": "../static/assert/morse_code_sounds/mcs-e.wav",
        "ans": "E",
        "prompt": "Which option is the corresponding letter?"
    },
    {
        "id": 2,
        "type": "input",
        "img": "../static/assert/quiz/quiz_images/quiz02Question.png",
        "img2": "",
        "questionName": "Type the right answer:",
        "placeholder": "Type the morse code",
        "audio": "../static/assert/morse_code_sounds/mcs-s.wav",
        "ans": "...",
        "prompt": "What is the Morse Code for this letter?"
    },
    {
        "id": 3,
        "type": "input",
        "img": "",
        "img2": "",
        "questionName": "Type the right answer:",
        "placeholder": "Type the letter",
        "audio": "../static/assert/morse_code_sounds/mcs-o.wav",
        "ans": "O",
        "prompt": "Listen to the audio. What letter is it?"
    },
    {
        "id": 4,
        "type": "selection",
        "img": "../static/assert/quiz/quiz_images/quiz04Question.png",
        "img2": "../static/assert/quiz/quiz_images/quiz04Question2.png",
        "questionName": "Select the right answer:",
        "placeholder": "",
        "audio": "../static/assert/morse_code_sounds/mcs-c.wav",
        "ans": "true",
        "prompt": "Are they a code/letter pair?"
    },
    {
        "id": 5,
        "type": "selection",
        "img": "",
        "img2": "",
        "questionName": "Select the right answer:",
        "placeholder": "",
        "audio": "../static/assert/morse_code_sounds/mcs-l.wav",
        "ans": "L",
        "prompt": "Which option is the corresponding letter?"
    },
    {
        "id": 6,
        "type": "selection",
        "img": "../static/assert/quiz/quiz_images/quiz06Question.png",
        "img2": "",
        "questionName": "Select the right answer:",
        "placeholder": "",
        "audio": "../static/assert/morse_code_sounds/mcs-r.wav",
        "ans": ".-.",
        "prompt": "Which option is the corresponding code?"
    },
    {
        "id": 7,
        "type": "selection",
        "img": "",
        "img2": "",
        "questionName": "type the right answer:",
        "placeholder": "type the morse code",
        "audio": "../static/assert/morse_code_sounds/mcs-m.wav",
        "ans": "--",
        "prompt": "Listen to the audio and write down the code."
    },
    {
        "id": 8,
        "type": "input",
        "img": "../static/assert/quiz/quiz_images/quiz08Question.png",
        "img2": "",
        "questionName": "type the right answer:",
        "placeholder": "type the word",
        "audio": "../static/assert/morse_code_sounds/mcs-sos.wav",
        "ans": "SOS",
        "prompt": "What is the word for these codes?"
    },
    {
        "id": 9,
        "type": "input",
        "img": "../static/assert/quiz/quiz_images/quiz09Question.png",
        "img2": "",
        "questionName": "type the right answer:",
        "placeholder": "Use spaces to separate letters",
        "audio": "",
        "ans": ".... . .-.. .--.",
        "prompt": "Write down the corresponding codes."
    },
    {
        "id": 10,
        "type": "input",
        "img": "",
        "img2": "",
        "questionName": "type the right answer:",
        "placeholder": "type the word",
        "audio": "../static/assert/morse_code_sounds/mcs-lmao.wav",
        "ans": "LMAO",
        "prompt": "Listen to the audio and write down the code."
    }
]

TOTAL_SOCRE = 0

user_learning_history = []

# ROUTES
@app.route('/')
def index():
    return redirect('home')

@app.route('/home')
def home():
    global user_learning_history
    history = (datetime.now(), "home page")
    user_learning_history.append(history)
    print(history)
    return render_template('home.html')

@app.route('/letters/0')
def letters():
    global user_learning_history
    history = (datetime.now(), "letter intro page")
    user_learning_history.append(history)
    print(history)
    return render_template('letters/letters.html')

@app.route('/letters/<id>')
def letters_letter(id=1):
    global learning_data
    global user_learning_history
    history = (datetime.now(), learning_data[int(id)-1]["letter"])
    user_learning_history.append(history)
    print(history)
    for letter in learning_data:
        if letter["id"] == int(id):
            return render_template('letters/letters_letter.html', data=learning_data, letter=letter)

@app.route('/words/1')
def words():
    global user_learning_history
    history = (datetime.now(), "HOPE")
    user_learning_history.append(history)
    print(history)
    return render_template('words/words_1.html')

@app.route('/words/2')
def words_2():
    global user_learning_history
    history = (datetime.now(), "PEACE")
    user_learning_history.append(history)
    print(history)
    return render_template('words/words_2.html')

@app.route('/quiz')
def quiz():
    global TOTAL_SOCRE
    TOTAL_SOCRE = 0
    return render_template('quiz/quiz.html')

@app.route('/quiz/final')
def quizFinal():
    global TOTAL_SOCRE
    return render_template('quiz/quizFinal.html', scores = TOTAL_SOCRE)

@app.route('/quiz/<id>')
def quiz_questions(id):
    global quiz_data
    global TOTAL_SOCRE

    for quiz in quiz_data:
        if quiz["id"] == int(id):
            return render_template('quiz/quiz' + id + '.html', data = quiz, id = id, scores = TOTAL_SOCRE)


@app.route('/quiz/check_ans/<qid>', methods=["GET", "Post"])
def check_ans(qid=None):
    '''
    Function to determin if user's anwer is correct or not
    Return correctness,
    '''
    global TOTAL_SOCRE
    global quiz_data

    ans = request.form["quiz"]
    print('ans =', ans) # ans = ImmutableMultiDict([('quiz1', 'P')])

    correctness = False
    question = [q for q in quiz_data if q["id"] == int(qid)]
    print('question =', question)
    if len(question) != 1:
        raise Exception("invalid question id")
    if ans.lower() == question[0]['ans'].lower():
        TOTAL_SOCRE += 1
        correctness = True

    result = {
        "id": question[0]["id"],
        "correctness": correctness,
        "ans": question[0]['ans'],
        "scores": TOTAL_SOCRE,
        "checked": ans
    }

    return jsonify(result)


if __name__ == '__main__':
   app.run(debug = True)
