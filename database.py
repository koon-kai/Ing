# coding: utf-8

import config

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

config = config.rec()
#engine = sa.create_engine(config.database + '?charset=utf8')
engine = sa.create_engine(config.db_url,convert_unicode=True,**config.db_conn_opt)

Session = sessionmaker()
Session.configure(bind = engine)
db = Session()

mBase = declarative_base()

def create_db():
    import models
    mBase.metadata.create_all(engine)
    print(u'数据库部署完成！')
    return
