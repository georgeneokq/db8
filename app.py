from flask import Flask, render_template

app = Flask(__name__, static_url_path='')

@app.route('/')
def db8():
  return render_template('db8-login.html')

@app.route('/login', methods=['POST'])
def login():
  return render_template('db8-login.html')