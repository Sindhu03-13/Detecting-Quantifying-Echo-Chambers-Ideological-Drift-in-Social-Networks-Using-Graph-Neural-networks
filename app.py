# app.py
from flask import Flask, request, jsonify, render_template
import random

app = Flask(_name_)

# Home page (frontend HTML)
@app.route('/')
def index():
    return render_template('index.html')

# Example backend API: detect echo chamber
@app.route('/detect', methods=['POST'])
def detect():
    text = request.form.get('post')
    # Mock logic: random "ideology drift" and "echo chamber" scores
    result = {
        "echo_chamber_score": round(random.uniform(0, 1), 2),
        "ideological_drift": round(random.uniform(0, 1), 2),
        "status": "Likely Echo Chamber" if random.random() > 0.5 else "Neutral"
    }
    return jsonify(result)

if _name_ == '_main_':
    app.run(debug=True)
