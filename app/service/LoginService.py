from flask import Flask, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_cors import *
from app.model.User import User
import uuid
from app.utils.message.SmsSend import send_sms
from app.utils.markets.QueryStockPrice import get_last_close
import random
from flask import request
import json
app = Flask(__name__)
# 跨域问题
CORS(app, supports_credentials=True)

msg_dict = {}

engine = create_engine('postgresql+psycopg2://Dolphin:ex4bFH9bmMz@106.14.196.51:5432/Dolphin')
DBSession = sessionmaker(bind=engine)

@app.route('/test', methods=['GET', 'POST'])
def limk_test():
    return jsonify({"code": 200, "state": "TESTING SUCCUSS..."})

@app.route('/login/<string:phone>/<string:verify_code>', methods=['GET'])
def login(phone, verify_code):
    session = DBSession()
    user = User(phone)
    if verify_code == msg_dict[phone]:
        return jsonify({"code": 200, "state": "SUCCUSS"})
    else:
        return jsonify({"code": 500, "state": "FAIL"})

@app.route('/verify/<string:phone>', methods=['GET'])
def verify_auth(phone):
    business_id = uuid.uuid1()
    # print("短线业务请求流水号：" + business_id)
    # 随机生成验证码
    random.seed = 1528621712
    random_num = random.randint(0,999999)
    # 补零填充六位
    random_code = random_num.__repr__().zfill(6)

    params = "{\"code\":\"%s\"}" % random_code
    print(business_id.__repr__() + "-->" + params)
    response = send_sms(business_id, phone, "数据分析爱好者", "SMS_135043260", params)

    code = json.loads(response.decode("utf-8"))['Code']
    print(code)
    if code == "OK":
        msg_dict[phone] = random_code
        return jsonify({"code": 200, "state": "SUCCUSS"})
    else:
        return jsonify({"code": 600, "state": "FAILD"})

def add_user(user, session):
    session.add(user)
    session.commit()


@app.route('/data', methods=['GET', 'POST'])
def get_data():
    code = request.json['code']
    start = request.json['start']
    end = request.json['end']
    print(code, start, end)
    data = get_last_close(code, start, end)
    return jsonify({"code": 200, "data": data})