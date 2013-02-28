# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String,Table,ForeignKey
from sqlalchemy.orm import relationship, backref
from database import mBase
import time

association_table = Table('association', mBase.metadata,
    Column('user_id', Integer, ForeignKey('user.id')),
    Column('board_id', Integer, ForeignKey('board.id'))
)

class Board(mBase):
    __tablename__ = 'board'
    __table_args__ = {
        'mysql_charset': 'utf8',
    }
    
    id = Column('id', Integer, primary_key=True,autoincrement = True)
    content = Column('content', String(200))
    user = relationship("User",secondary=association_table,backref="boards")
    create_date = Column('create_date',Integer)

    def __init__(self,content):
        self.content = content
        if create_date == None:
            self.create_date = int(time.time())
        else:
            self.create_date = create_date

    def __unicode__(self):
        return self.content

    def __repr__(self):
        return '<Board %s>' % (self.content)  