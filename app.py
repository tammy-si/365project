from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    connect = sqlite3.connect('boxoffice.db')
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM Movie')

    data = cursor.fetchall()
    return render_template('index.html', data=data)


@app.route('/drop')
def drop():
    return render_template('drop.html')


if __name__ == '__main__':
    app.run(debug=True)
