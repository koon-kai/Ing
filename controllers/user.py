# coding: utf-8


import config
from .base import BaseHandler
from database import db
from models import User
from werkzeug import check_password_hash, generate_password_hash

config = config.rec()

class LoginHandler(BaseHandler):
    def get(self):
        if self.isLogin():
            self.redirect("/index")
        else:
            self.render("login.html",error=u'请登录')

    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        user = db.query(User).filter_by(name =username).first()
        error = None
        if user is None:
            error = 'Invalid username'
        elif not check_password_hash(user.pw_hash,password):
            error = 'Invalid password'
        else:
            self.set_cookie("user_id",user.id)
            self.set_cookie("email",user.email)
            self.currentUserSet(username)
            self.redirect("/index")
        self.render("login.html",error=error)

class LogoutHandler(BaseHandler):
    def get(self):
        self.clear_cookie('user')
        self.redirect('/login')


class RegisterHandler(BaseHandler):
    def get(self):
        if self.isLogin():
            self.redirect("/index")
        else:
            self.render("register.html")

    def post(self):
        username = self.get_argument("username")
        email = self.get_argument("email")
        password = self.get_argument("password")
        confirm_password = self.get_argument("confirm_password")

        db.add(User(name=username,email=email,pw_hash= generate_password_hash(password)))
        db.commit()
        #self.set_cookie("email",email)
        #self.currentUserSet(username)
        self.redirect("/login")

