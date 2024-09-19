from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
    temperature = random.uniform(20.0, 25.0)
    return render_template('index.html', temperature=temperature)

if __name__ == '__main__':
    app.run(debug=True)