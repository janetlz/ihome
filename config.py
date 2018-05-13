# coding=utf-8
import redis


class Config(object):
    """配置类"""
    BEBUG = True

    # 设置 SECRET_KEY
    SECRET_KEY = ''  # (自动生成)

    # mysql数据库的相关设置
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1/ihome_lz"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # redis 配置项
    REDIS_HOST = "127.0.0.1"  # redis命令行地址
    REDIS_PORT = 6379

    # session 的配置存储在redis
    SESSION_TYPE = "redis"
    # session存储到哪个redis里面
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    # 开启session的签名（也就是要不要隐藏session信息，加密）
    SESSION_USE_SIGNER = True
    # 设置过期时间
    PERMANENT_SESSION_LIFETIME = 86400 * 6  # 默认为一个月


class DevelopmentConfig(Config):
    """开发环境中配置累"""
    DEBUG = True


class ProductionConfig(Config):
    """生产环境中的配置类"""
    # 设置数据库链接地址
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1/ihome_lz"


class TestingConfig(Config):
    """测试环境中的配置类"""
    # 设置数据库链接地址
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1/Test_ihome_lz"
    # 开启测试标志
    TESTING = True


config_dict = {
    "development": DevelopmentConfig,
    'production': ProductionConfig,
    "testing": TestingConfig
}
