# encoding=utf-8

from flask import Flask,url_for
from werkzeug.routing import BaseConverter

app=Flask(__name__)
# app.config.from_pyfile('setting.cfg')

class MyConfig():
    DEBUG = True

app.config.from_object(MyConfig)
# @app.route("/index")
# def shouye():
#     return "shouye"
@app.route("/index")
def index():
    return u"首页"
#
# @app.route("/index")
# def index1():
#     return "first ye"

class ReCoverter(BaseConverter):
    def __init__(self,url_map,*args):
        super(ReCoverter,self).__init__(url_map)
        self.regex=args[0]
    def to_python(self, value):
        print(value)
        return value
    def to_url(self, value):
        print (value)
        return value
app.url_map.converters["re"]=ReCoverter

@app.route("/login",methods=["post","get"])
def login():
    return u"登陆"
@app.route("/zhuce",methods=["post","get"])
@app.route("/register",methods=["post","get"])
def register():
    return "<a href=%s>index<\a>" % url_for("index")
@app.route("/id/<int:id>")
def get_id(id):
    return "id=%s"%id
@app.route('/page/<re("\d{3}"):page>')
def page(page):
    return "page=%s"%page
@app.route("/author")
def auther():
    return "<a href=%s>page</a>"%url_for("page",page="123")


if __name__ == "__main__":
    app.run("0.0.0.0",port=5000)