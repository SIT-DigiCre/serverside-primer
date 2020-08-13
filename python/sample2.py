#!/usr/bin/env python3
from flask import Flask, session, request

app = Flask(__name__)
HTMLHEAD = """
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <title>Access counter</title>
        <meta content="text/html; charset=utf-8" http-equiv="content-type" />
        <meta content="width=device-width, initial-scale=1" name="viewport" />
    </head>
    <body>
        <form action="" method="post">
"""
HTMLFOOT = """
            <p><input type="submit" value="reset" /></p>
        </form>
    </body>
</html>
"""

@app.route("/", methods=["get", "post"])
def numguess():
    # もしリクエストメソッドがPOSTだった、またはセッション情報がセットされていなかった場合
    if (request.method == "POST" or "count" not in session):
        # セッション情報を0で初期化
        session["count"] = 0
    else:
        session["count"] += 1
    return (HTMLHEAD + "<p>" + str(session["count"]) + "</p>" + HTMLFOOT)

app.secret_key = "がっこうぐらし！"
app.run(host="0.0.0.0", port=8000)
