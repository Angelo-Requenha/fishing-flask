from flask import Flask
from funcoes import criaBanco

app = Flask(__name__)
criaBanco()

from routes import *

if __name__ == "__main__":
    app.run(debug=True)