import random
import uuid
from app.utils.message.SmsSend import send_sms
import json
from app.service.LoginService import msg_dict

# 随机生产六位短信验证码
def createAuthCode():
    # 设置随机数种子
    random.seed = 1528621712
    # 随机生成一个0～999999的数字
    random_num = random.randint(0, 999999)
    # 高位补零填充满六位
    random_code = random_num.__repr__().zfill(6)
    return random_code

# 那短信服务器请求发送短信
def sendSmsRequest(phone):
    # 生成短线业务请求流水号
    business_id = uuid.uuid1()
    random_code = createAuthCode()
    # 请求参数
    params = "{\"code\":\"%s\"}" % random_code
    print(business_id.__repr__() + "-->" + params)
    # 发送请求
    response = send_sms(business_id, phone, "数据分析爱好者", "SMS_135043260", params)
    status_code = json.loads(response.decode("utf-8"))['Code']
    if(status_code == 'OK'):
        msg_dict[phone] = random_code
    return {'status_code':status_code, 'random_code':random_code}