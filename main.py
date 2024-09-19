from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def login():
    return render_template('login.html')


@app.route('/selection.html')
def selection():
    return render_template('selection.html')


if __name__ == '__main__':
    app.run(debug=True)
