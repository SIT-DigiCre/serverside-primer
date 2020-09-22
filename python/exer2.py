#!/usr/bin/env python3
from flask import Flask, session, request, render_template
import random

app = Flask(__name__)

@app.route("/janken", methods=["GET", "POST"])
def janken():
    # sessionの初期化
    if "userwin" not in session:
        session["userwin"] = 0
    if "computerwin" not in session:
        session["computerwin"] = 0

    if request.method == "POST":
        if request.form["rps"] == "グー":
            userrps = 0
        elif request.form["rps"] == "チョキ":
            userrps = 1
        elif request.form["rps"] == "パー":
            userrps = 2

        comrps = random.randint(0, 2)
        status = "あなたの手: " + request.form["rps"] + ", コンピュータの手: "
        if comrps == 0:
            status += "グー"
        elif comrps == 1:
            status += "チョキ"
        elif comrps == 2:
            status += "パー"

        # TODO: sessionに勝った回数を格納する
        if userrps - comrps == 0:
            result = "あいこ！"
        elif userrps - comrps == -1 or userrps - comrps == 2:
            result = "あなたの勝ち！"
            # ヒント
            # session["userwin"] += 1
        else:
            result = "コンピュータの勝ち！"
            # session["computerwin"]

        # TODO: sessionの情報を文字列として出力する
        winlose = "あなたの{}勝{}敗".format("", "")
        return render_template("exer2.html", status=status, result=result, winlose=winlose)
    else:
        return render_template("exer2.html", status="", result="", winlose="")

app.secret_key = "がっこうぐらし！"
app.run(host="0.0.0.0", port=8000)
