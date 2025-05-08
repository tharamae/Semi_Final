import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Thara Mae C. Tuñacao <br> BSIT-3 1st 25 <br> System Integration and Architecture 1 <br> Semi-Final Exam'

if __name__=='__main__':
    port = int(os.environ.get("PORT",5000))
    app.run(host='0.0.0.0', port=port)