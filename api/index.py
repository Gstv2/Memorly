from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__, static_folder = 'static')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == 'main':
    app.run(debug=True)