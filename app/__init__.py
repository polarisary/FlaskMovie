from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)  # 创建app对象
app.debug = True  # 开启调试模式
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@127.0.0.1:3306/movie"  # 定义数据库连接，传入连接，默认端口3306，可不写
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root:root@127.0.0.1:3306/movie"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

# 定义db对象，实例化SQLAlchemy，传入app对象
db = SQLAlchemy(app)

from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint

# 注册蓝图
app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint, url_prefix="/admin")


# 添加全局404页面
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
