from flask import Flask

app = Flask(__name__)

from app import routes

#if name == "main":
#    app.run(host='0.0.0.0'), port = 5000)
