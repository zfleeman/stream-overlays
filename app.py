from flask import Flask, render_template, url_for
import random

app = Flask(__name__)

@app.route('/questions')
def questions_page():
    with open('questions/new.txt') as f:
        questions = [line.rstrip() for line in f]

    questions = list(set(questions))
    random.shuffle(questions)
    question = questions.pop()

    with open('questions/old.txt', 'a') as f:
        f.write("%s\n" % question)

    with open('questions/new.txt', 'w') as f:
        f.writelines("%s\n" % q for q in questions)
    
    return render_template('horsequestions/index.html', question = question)

@app.route('/poewheel')
def poewheel_page():
    masque = ['poewheel/masque/masque_04.mp3', 'poewheel/masque/masque_10.mp3', 'poewheel/masque/masque_11.mp3', 'poewheel/masque/masque_05.mp3', 'poewheel/masque/masque_13.mp3', 'poewheel/masque/masque_07.mp3', 'poewheel/masque/masque_06.mp3', 'poewheel/masque/masque_12.mp3', 'poewheel/masque/masque_02.mp3', 'poewheel/asque/masque_03.mp3', 'poewheel/masque/masque_01.mp3', 'poewheel/masque/masque_15.mp3', 'poewheel/masque/masque_14.mp3', 'poewheel/masque/masque_08.mp3', 'poewheel/masque/masque_09.mp3']
    bells = ['poewheel/bells/bells_04.mp3', 'poewheel/bells/bells_01.mp3', 'poewheel/bells/bells_02.mp3', 'poewheel/bells/bells_03.mp3']
    heart = ['poewheel/telltale/telltale_09.mp3', 'poewheel/telltale/telltale_08.mp3', 'poewheel/telltale/telltale_06.mp3', 'poewheel/telltale/telltale_07.mp3', 'poewheel/telltale/telltale_05.mp3', 'poewheel/telltale/telltale_04.mp3', 'poewheel/telltale/telltale_10.mp3', 'poewheel/telltale/telltale_01.mp3', 'poewheel/telltale/telltale_03.mp3', 'poewheel/telltale/telltale_02.mp3']
    raven = ['poewheel/theraven/theraven_09.mp3', 'poewheel/theraven/theraven_08.mp3', 'poewheel/theraven/theraven_18.mp3', 'poewheel/theraven/theraven_14.mp3', 'poewheel/theraven/theraven_01.mp3', 'poewheel/theraven/theraven_15.mp3', 'poewheel/theraven/theraven_03.mp3', 'poewheel/theraven/theraven_17.mp3', 'poewheel/theraven/theraven_16.mp3', 'poewheel/theraven/theraven_02.mp3', 'poewheel/theraven/theraven_06.mp3', 'poewheel/theraven/theraven_12.mp3', 'poewheel/theraven/theraven_13.mp3', 'poewheel/theraven/theraven_07.mp3', 'poewheel/theraven/theraven_11.mp3', 'poewheel/theraven/theraven_05.mp3', 'poewheel/theraven/theraven_04.mp3', 'poewheel/theraven/theraven_10.mp3']
    cask = ['poewheel/cask/cask_08.mp3', 'poewheel/cask/cask_09.mp3', 'poewheel/cask/cask_10.mp3', 'poewheel/cask/cask_04.mp3', 'poewheel/cask/cask_05.mp3', 'poewheel/cask/cask_11.mp3', 'poewheel/cask/cask_07.mp3', 'poewheel/cask/cask_12.mp3', 'poewheel/cask/cask_06.mp3', 'poewheel/cask/cask_02.mp3', 'poewheel/cask/cask_03.mp3', 'poewheel/cask/cask_01.mp3']
    haunt = ['poewheel/haunt/haunt_02.mp3', 'poewheel/haunt/haunt_01.mp3']
    eldorado =['poewheel/eldorado/eldorado.mp3']
    dream = ['poewheel/dream/dream.mp3']

    random.shuffle(masque)
    random.shuffle(bells)
    random.shuffle(heart)
    random.shuffle(raven)
    random.shuffle(cask)
    random.shuffle(haunt)
    random.shuffle(eldorado)
    random.shuffle(dream)

    return render_template('poewheel/index.html',
        speakr = url_for('static', filename = raven.pop()),
        speakm = url_for('static', filename = masque.pop()),
        speakb = url_for('static', filename = bells.pop()),
        speakh = url_for('static', filename = heart.pop()),
        speakc = url_for('static', filename = cask.pop()),
        speakha = url_for('static', filename = haunt.pop()),
        speakd = url_for('static', filename = dream.pop()),
        speakel = url_for('static', filename = eldorado.pop())
    )

@app.route('/25ravens')
def ravens25():
    return render_template('ravens/25.html')

@app.route('/250ravens')
def ravens250():
    return render_template('ravens/250.html')

if __name__ == '__main__':
    app.run(debug=True, port=3030, host='0.0.0.0')
