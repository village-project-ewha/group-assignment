from flask import Flask, render_template, request
from database import DBhabdler
import sys

application = Flask(__name__)

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

@application.route("/submit_item_post", methods=['POST'])
def submit_item_post():

    image_file=request.files["file"]
    image_file.save("static/images/{}".format(image_file.filename))
    data=request.form
    DB.insert_item(data['name'], data, image_file.filename) #key값 지정하고 value 넣기

    return render_template("submit_item_result.html", data=data, img_path="static/images/{}".format(image_file.filename))

    
if __name__ == "__main__":
    application.run(host='0.0.0.0', debug=True)