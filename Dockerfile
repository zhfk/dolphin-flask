## docker login --username=17601305266 registry.cn-shanghai.aliyuncs.com
## docker build -t registry.cn-shanghai.aliyuncs.com/zhfk/registry-dolphin-flask:latest .
## docker push registry.cn-shanghai.aliyuncs.com/zhfk/registry-dolphin-flask:latest

FROM python:3.5.5-jessie
RUN pip install sqlalchemy flask_cors flask flask_sqlalchemy
RUN apt-get update
RUN apt-get install -y postgresql
RUN pip install psycopg2-binary
RUN mkdir -p /root/dolphin/dolphin-flask
COPY . /root/dolphin/dolphin-flask
WORKDIR  /root/dolphin
ENTRYPOINT python dolphin-flask/com/dolphin/yehui/LoginService.py