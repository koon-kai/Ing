import tornado.httpserver
import tornado.ioloop
import tornado.web
import config



config = config.rec()

class BaseHandler(tornado.web.RequestHandler):
    def on_finish(self):
        None

    def currentUserGet(self):
        username = self.get_secure_cookie("user")
        if username:
            return tornado.escape.json_decode(username)
        else:
            return None

    def currentUserSet(self, username):
        if username:
            self.set_secure_cookie("user",
                    tornado.escape.json_encode(username))
        else:
            self.clear_cookie("user")

    def replyerSet(self, name, email, website):
        if name:
            self.set_secure_cookie("replyer",
                    tornado.escape.json_encode({'name': name, 'email': email,
                        'website': website}))
        else:
            self.clear_cookie("replyer")

    def replyerGet(self):
        name = self.get_secure_cookie("replyer")
        if name:
            return tornado.escape.json_decode(name)
        else:
            return None

    def isLogin(self):
        username = self.currentUserGet()
        if username:
            return True
        else:
            return False

    def checkLogin(self):
        if not self.isLogin():
            raise tornado.web.HTTPError(404)

    def get_current_user(self):
        return self.currentUserGet()
