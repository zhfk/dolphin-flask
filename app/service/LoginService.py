from app.utils.database.Connect import *

# 保存手机登录验证码的字典
global msg_dict
msg_dict = {}

# 验证码校验登录
def login(phone, verify_code):
    # 短信校验成功
    if msg_dict[phone] == verify_code:
      # 查询用户是否已注册
      user = query_user(phone)
      # 用户未注册自动注册
      if user:
        print("用户未注册")
        user = User(phone)
        add_user(user)
      # 清空用户对用的验证码
      msg_dict.pop(phone)
      return True
    else:
        return False
