# coding=utf-8
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from ihome import create_app,db

# 需求，不修改业务逻辑的代码，，只通过修改manager文件
# 中的一句代码获取不同配置环境中的app
app = create_app('production')


# 创建Manage管理对象 ---脚本方式管理对象
manager = Manager(app)
Migrate(app,db)
# 添加迁移命令
manager.add_command('db',MigrateCommand)


@app.route('/', methods=['GET', 'POST'])
def index():
    # session["name"]= 'itheima'

    return 'index'


if __name__ == '__main__':
    # 运行开发web服务器
    # app.run()
    manager.run()
