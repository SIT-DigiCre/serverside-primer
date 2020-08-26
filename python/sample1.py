#!/usr/bin/env python3
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def welcome():
    # もしクエリパラメータのnameがセットされており、かつ長さが0以上だった場合
    if ("name" in request.args and len(request.args["name"]) > 0):
        # Hello, [名前]をクライアントに返す
        return render_template("sample1.html", greetings="Hello, " + request.args["name"] + ".")
    # Welcome, anonymousをクライアントに返す
    return render_template("sample1.html", greetings="Welcome, anonymous.")

app.run(host="0.0.0.0", port=8000)
