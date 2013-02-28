# coding: utf-8
import os

_basedir = os.path.abspath(os.path.dirname(__file__))

_DBUSER = "root" # 数据库用户名
_DBPASS = "root" # 数据库密码
_DBHOST = "localhost" # 数据库地址
_DBNAME = "ing" # 数据库名称

class rec: pass

rec.database = 'mysql://%s:%s@%s/%s' % (_DBUSER, _DBPASS, _DBHOST,_DBNAME)
rec.cookie_secret = 'IngTodolist'
rec.title = u"RememberMe"
rec.url = 'http://www.example.com/'
rec.default_timezone = "Asia/Shanghai"

rec.db_url = 'sqlite:///' + os.path.join(_basedir, 'Ing.db')
rec.db_conn_opt  = {}