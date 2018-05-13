# coding=utf-8
import redis
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from config import Config
from flask import Flask
from config import config_dict

# 创建SQAlchemy对象
db = SQLAlchemy()


# 工厂方法
def create_app(config_name):
    # 创建Flask应用程序实例
    app = Flask(__name__)

    # 获取配置类
    config_cls = config_dict[config_name]
    app.config.from_object(config_cls)

    # db对象进行app的关联
    db.init_app(app)

    # 创建redis 数据库链接对象
    redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)

    # 开启CSRF 验证保护
    # 只做保护校验，至于生成CSEF_TOKEN cookie 还有请求时，携带csef_token 需要自己来完成
    CSRFProtect(app)

    # # Session信息存储
    Session(app)
