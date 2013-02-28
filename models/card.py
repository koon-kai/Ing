# -*- coding: utf-8 -*-
from sqlalchemy import  Column, Integer, String, DateTime,Text
from database import mBase
import time


class Card(mBase):
    __tablename__ = 'card'
    __table_args__ = {
        'mysql_charset': 'utf8',
    }
    
    id = Column('id', Integer, primary_key=True,autoincrement = True)
    content = Column('content', Text)
    describe = Column('describe',Text)
    user_id = Column('user_id',Integer,index=True)
    board_id = Column('board_id',Integer,index=True)
    card_type = Column('card_type',Integer)
    remind_date = Column('remind_date',Integer)
    create_date = Column('create_date',Integer)

    def __init__(self,name,user_id):
        self.name = name
        self.user_id = user_id
        if create_date == None:
            self.create_date = int(time.time())
        else:
            self.create_date = create_date

    def __unicode__(self):
        return self.id

    def __repr__(self):
        return '<Board %s>' % (self.id)  