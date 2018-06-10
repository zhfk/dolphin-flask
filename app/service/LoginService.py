from flask import Flask, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_cors import *
from app.bean.User import User
import uuid
from app.message.SmsSend import send_sms
import random
import json
app = Flask(__name__)
# 跨域问题
CORS(app, supports_credentials=True)

msg_dict = {}

engine = create_engine('postgresql+psycopg2://Dolphin:ex4bFH9bmMz@106.14.196.51:5432/Dolphin')
DBSession = sessionmaker(bind=engine)

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

def add_user(user,session):
    session.add(user)
    session.commit()

# def query_all():
#     query = session.query(User).all()
#     return query
#
# def query_by_phone(phone):
#     query = session.query(User).filter(User.phone == phone).all()
#     return query
#
# def query_by_name(nick_name):
#     query = session.query(User).filter(User.nick_name == nick_name).all()
#     return query

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9966)
