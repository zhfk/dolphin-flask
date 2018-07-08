from flask import Flask
from flask_cors import *

# app = Flask(__name__)
# # 跨域问题
# CORS(app, supports_credentials=True)

from app.service.LoginService import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9966)



