from flask import render_template
from app import app

print('oi')
@app.route('/')
def index():
    return render_template('index.html')