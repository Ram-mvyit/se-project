from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='template')

# correct answer
correct_answer = "b"

@app.route('/')
def login():
    return render_template("login.html")

@app.route('/dashboard', methods=['POST'])
def dashboard():
    username = request.form['username']
    return render_template("dashboard.html", username=username)

@app.route('/exam')
def exam():
    return render_template("exam.html")

@app.route('/submit', methods=['POST'])
def submit():
    answer = request.form['q1']

    if answer == correct_answer:
        score = 1
    else:
        score = 0

    return render_template("result.html", score=score)

if __name__ == '__main__':
    app.run(debug=True, host= "127.0.0.1", port=1326)