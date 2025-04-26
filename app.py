
from flask import Flask, render_template, request, jsonify
from zxcvbn import zxcvbn
import random
import string

app = Flask(__name__)

def generate_password(length=16, use_symbols=True, avoid_ambiguous=True):
    letters = string.ascii_letters
    digits = string.digits
    symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    ambiguous = "l1O0"

    all_chars = letters + digits
    if use_symbols:
        all_chars += symbols
    if avoid_ambiguous:
        for ch in ambiguous:
            all_chars = all_chars.replace(ch, "")

    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    length = random.randint(12, 24)
    password = generate_password(length)
    return jsonify(password=password, length=length)

@app.route('/strength', methods=['POST'])
def strength():
    data = request.json
    password = data.get("password", "")
    result = zxcvbn(password)

    score = result["score"]
    feedback = result["feedback"]["warning"] or "Looks good!"
    guesses_per_sec = 1e9
    crack_time_sec = float(result["guesses"]) / guesses_per_sec
    years = crack_time_sec / (60 * 60 * 24 * 365)

    if years > 1e9:
        crack_time = "∞ (Too long)"
    elif years < 1:
        crack_time = "< 1 year"
    else:
        crack_time = f"{years:.1f} years"

    return jsonify(score=score, feedback=feedback, crack_time=crack_time)

if __name__ == '__main__':
    app.run(debug=True)
