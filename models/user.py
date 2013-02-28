# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, DateTime
from database import mBase


class User(mBase):
    __tablename__ = 'user'
    __table_args__ = {
        'mysql_charset': 'utf8',
    }

    id = Column('id', Integer, primary_key=True,autoincrement = True)
    name = Column('user_name', String(200))
    email = Column('email',String(200))
    pw_hash = Column('pw_hash',String(200))

    def __init__(self,name,email,pw_hash):
        self.name = name
        self.email = email
        self.pw_hash = pw_hash

    def __unicode__(self):
        return self.name

    def __repr__(self):
        return '<User %s>' % (self.name)  