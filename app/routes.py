from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def hello_world():
    user = {'username': 'Dascha'}
    return render_template('index.html', title='Home', user=user)
