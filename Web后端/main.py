import os
from flask import Flask, jsonify, request, json, session
from flask_cors import CORS
from gevent import monkey
from gevent.pywsgi import WSGIServer
from userMgmt.userLink.userRouter import user
from userMgmt.userLink.verificationCode import api

monkey.patch_all()

app = Flask(__name__)


app.register_blueprint(user)
app.register_blueprint(api)
app.secret_key = 'zxdsb'
CORS(app)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run()
    http_sever = WSGIServer(('', 5000), app)
    http_sever.serve_forever()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
