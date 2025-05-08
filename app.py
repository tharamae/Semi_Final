from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Thara Mae C. Tuñacao <br> BSIT-3 1st 25 <br> System Integration and Architecture 1 <br> Semi-Final Exam'

