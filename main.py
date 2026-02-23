import os
from datetime import datetime
import jinja2
from flask import Flask, url_for, session, request, render_template

app = Flask(__name__)

@app.route('/<string:title>')
@app.route('/index/<string:title>')
def index(title):
    return render_template('index.html', title=title)


if __name__ == '__main__':
    app.secret_key = 'super-secure-secret-key'
    app.run(host='0.0.0.0', port=8080)
