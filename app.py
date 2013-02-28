# coding: utf-8
import os.path
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.options

import config
from controllers import user,index
from database import create_db
from helpers import getAvatar

config = config.rec()

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", index.HomeHandler),
            (r"/index[/]*", index.IndexHandler),

            (r"/login[/]*", user.LoginHandler),
            (r"/logout[/]*", user.LogoutHandler),
            (r"/register[/]*", user.RegisterHandler),

        ]
        settings = dict(
            template_path = os.path.join("templates"),
            static_path = os.path.join("static"),
            xsrf_cookies = True,
            cookie_secret = config.cookie_secret,
            autoescape = None,
            title = config.title,
            url = config.url,
            login_url = "/",
            debug=True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)

def main():
    #create_db()
    print("App started. Listenning on %d" % int(os.environ.get('PORT', 8888)))
    tornado.options.parse_command_line()
    tornado.httpserver.HTTPServer(Application()).listen(int(os.environ.get('PORT',8888)))
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()
