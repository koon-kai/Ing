# coding: utf-8

import config
from .base import BaseHandler
from helpers import formatText,getAvatar
from database import db
import markdown
from models import Board,User



config = config.rec()


class HomeHandler(BaseHandler):
    def get(self):
        self.render("home.html")


class IndexHandler(BaseHandler):
    def get(self):
        email = self.get_cookie("email")
        user_id = self.get_cookie("user_id")
        #boards = db.query(Board).filter(Board.user.any(User.id.in_(user_id))).all()
        #print boards
        self.render("index.html",email=email,getAvatar=getAvatar)
