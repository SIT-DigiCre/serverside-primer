#!/usr/bin/env python3
from flask import Flask, session, request
import random

app = Flask(__name__)
PORT = 8800
HTMLHEAD = """
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <title>Guess Number</title>
        <meta content="text/html; charset=utf-8" http-equiv="content-type" />
        <meta content="width=device-width, initial-scale=1" name="viewport" />
    </head>
    <body>
        <form action="" method="post">
"""
HTMLFOOT = """
            <p>Input Your Guess: <input type="text" name="num" /></p>
            <p><input type="submit" /></p>
        </form>
    </body>
</html>
"""

@app.route("/numguess", methods = ["get", "post"])
def numguess():
    res = ""
    if ("rnum" not in session):
        session["rnum"] = str(random.randint(1, 100))
        session["count"] = str(0)
    if (request.method == "POST" and "num" in request.form):
        try:
            num = int(request.form["num"])
            rnum = int(session["rnum"])
            count = int(session.get("count"))
            count += 1
            session["count"] = str(count)
            res = "<p>" + str(count) + "tries, " + str(num) + ": "
            if (num < rnum):
                res += "small!</p>"
            elif (num > rnum):
                res += "big!</p>"
            else:
                res += "Congratulations!</p>"
                session.pop("rnum")
                session.pop("count")
        except:
            res = "<p>error</p>"
    return (HTMLHEAD + res + HTMLFOOT)

app.secret_key = "がっこうぐらし！"
app.run(host = "0.0.0.0", port = 8800)
