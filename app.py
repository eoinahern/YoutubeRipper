from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "GET":
        return render_template("main_page.html")
    else:
        url = request.form.get("url")
        #fake data!!!
        data = ["http://www.google.com", "http://www.facebook.com"]
        return render_template("search_complete.html", data=data)




def authURL(url):
    pass
