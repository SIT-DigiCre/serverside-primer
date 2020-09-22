#!/usr/bin/env python3
from flask import Flask, session, request, render_template

app = Flask(__name__)

@app.route("/countup", methods=["get", "post"])
def countup():
    # もしリクエストメソッドがPOSTだった、またはセッション情報がセットされていなかった場合
    if (request.method == "POST" or "count" not in session):
        # セッション情報を0で初期化
        session["count"] = 0
    else:
        session["count"] += 1
    return render_template("sample2.html", count=str(session["count"]))

app.secret_key = "がっこうぐらし！"
app.run(host="0.0.0.0", port=8000)
