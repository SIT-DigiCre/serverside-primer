#!/usr/bin/env python3
from flask import Flask, request
import random

app = Flask(__name__)
PORT = 8800
HTMLHEAD = """
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <title>じゃんけん</title>
        <meta content="text/html; charset=utf-8" http-equiv="content-type" />
        <meta content="width=device-width, initial-scale=1" name="viewport" />
    </head>
    <body>
        <h1>じゃんけん！</h1>
        <form action="" method="post">
"""
HTMLFOOT = """
            <p><input type="submit" name="rps" value="グー" /></p>
            <p><input type="submit" name="rps" value="チョキ" /></p>
            <p><input type="submit" name="rps" value="パー" /></p>
        </form>
    </body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def rps():
    if request.method == "POST":
        if request.form["rps"] == "グー":
            userrps = 0
        elif request.form["rps"] == "チョキ":
            userrps = 1
        elif request.form["rps"] == "パー":
            userrps = 2

        comrps = random.randint(0, 2)
        status = "<p>あなたの手: " + request.form["rps"] + ", コンピュータの手: "
        if comrps == 0:
            status += "グー"
        elif comrps == 1:
            status += "チョキ"
        elif comrps == 2:
            status += "パー"
        status += "</p>"

        if userrps - comrps == 0:
            result = "<p>あいこ！</p>"
        elif userrps - comrps == -1 or userrps - comrps == 2:
            result = "<p>あなたの勝ち！</p>"
        else:
            result = "<p>コンピュータの勝ち！</p>"
        return (HTMLHEAD + status + result + HTMLFOOT)
    else:
        return (HTMLHEAD + HTMLFOOT)

app.run(host = "0.0.0.0", port = 8800)
