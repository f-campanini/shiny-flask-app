from ddtrace import tracer
from flask import Flask, render_template, request, redirect, url_for
import logging
import os

app = Flask(__name__)

@app.route('/')
def index():
    # logger.info("This log is from the index route Hello, world" + logger.name)
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save(uploaded_file.filename)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='4444')