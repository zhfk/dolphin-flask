from flask import Flask, json, make_response
from flask_cors import *
from app.utils.markets.QueryStockPrice import get_period_close
from flask import request
from app.service.VerifyService import sendSmsRequest
from app.service.LoginService import login as login_verify
import datetime
app = Flask(__name__)
# 跨域问题
CORS(app, supports_credentials=True)


@app.route('/test', methods=['GET', 'POST'])
def link_test():
    response_data = {"state": "SUCCUSS", "data": "Test Connected..."}
    response = make_response(json.dumps(response_data))
    response.mimetype = "application/json"
    return response

@app.route('/login', methods=['GET', 'POST'])
def login():
    phone = request.json['phone']
    verify_code = request.json['verify_code']
    state = login_verify(phone, verify_code)
    if state:
        response_data = {"state": "SUCCUSS", "data": "Login success..."}
        response = make_response(json.dumps(response_data))
        response.mimetype = "application/json"
        outdate = datetime.datetime.now() + datetime.timedelta(hours=0.5)
        response.set_cookie('phone', phone, expires=outdate)
        return response
    else:
        response_data = {"state": "FAIL", "data": "Login faild..."}
        response = make_response(json.dumps(response_data))
        response.mimetype = "application/json"
        return response

@app.route('/verify', methods=['GET', 'POST'])
def send_verify_code():
    phone = request.json['phone']
    res = sendSmsRequest(phone)
    if res['status_code'] == "OK":
        response_data = {"state": "SUCCESS", "data": "Send message success..."}
        response = make_response(json.dumps(response_data))
        response.mimetype = "application/json"
        return response
    else:
        response_data = {"state": "FAILD", "data": "Send message faild..."}
        response = make_response(json.dumps(response_data))
        response.mimetype = "application/json"
        return response


# 根据股票代码和周期获得行情数据
# param: code, startdate, enddate
@app.route('/data/period', methods=['GET', 'POST'])
def get_data():
    code = request.json['code']
    start = request.json['start']
    end = request.json['end']
    phone = request.cookies.get("phone")
    if phone:
        data = get_period_close(code, start, end)
        response_data = {"state": "SUCCESS", "data": data}
        response = make_response(json.dumps(response_data))
        response.mimetype = "application/json"
        return response
    else:
        response_data = {"state": "FAILD", "data": "not login..."}
        response = make_response(json.dumps(response_data))
        response.mimetype = "application/json"
        return response