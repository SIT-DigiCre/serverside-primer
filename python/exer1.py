#!/usr/bin/env python3
from flask import Flask, request, render_template
import random

app = Flask(__name__)

@app.route("/janken", methods=["GET", "POST"])
def janken():
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

        # TODO: resultにじゃんけんの結果を格納する
        result = ""
        # ヒント
        # if userrps - comrps == 0:
        #     result = "あいこ！"

        return render_template("exer1.html", status=status, result=result)
    else:
        return render_template("exer1.html", status="", result="")

app.run(host="0.0.0.0", port=8000)
