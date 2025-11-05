from flask import Flask, render_template, request, flash, redirect, url_for, session
from database import DBhabdler
import hashlib
import sys

application = Flask(__name__)
application.config["SECRET_KEY"] = "helloosp"

DB = DBhabdler()

#내 웹페이지의 홈 ("/")을 만날 때마다 Hello my webpage!를 출력하게 됨
@application.route("/")
def hello():
    return render_template("index.html")
    #return "Hello my webpage!"

@application.route("/list")
def view_list():
    return render_template("list.html")

@application.route("/product_detail")
def product_detail():
    return render_template("product_detail.html")

@application.route("/products")
def view_products():
    return render_template("products.html")

@application.route("/review")
def view_review():
    return render_template("review.html")

@application.route("/reg_items")
def reg_item():
    return render_template("reg_items.html")

@application.route("/reg_reviews")
def reg_review():
    return render_template("reg_reviews.html")

@application.route("/login")
def login():
    return render_template("login.html")

@application.route("/signup")
def signup():
    return render_template("signup.html")

@application.route("/signup_post", methods=['POST'])
def register_user():
    data=request.form
    pw=request.form['pw']
    pw_hash = hashlib.sha256(pw.encode('utf-8')).hexdigest()    #id 중복 체크 필요
    if DB.insert_user(data,pw_hash):
        return render_template("login.html")
    else:   # 중복 아이디 존재 시 플래시 메세지 띄움
        flash("user id already exist!")
        return render_template("signup.html")

@application.route("/submit_item_post", methods=['POST'])
def submit_item_post():

    image_file=request.files["file"]
    image_file.save("static/images/{}".format(image_file.filename))
    data=request.form
    DB.insert_item(data['name'], data, image_file.filename) #key값 지정하고 value 넣기

    return render_template("submit_item_result.html", data=data, img_path="static/images/{}".format(image_file.filename))

    
if __name__ == "__main__":
    application.run(host='0.0.0.0', debug=True)