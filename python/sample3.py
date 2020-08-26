#!/usr/bin/env python3
from flask import Flask, session, request, render_template
import random

app = Flask(__name__)

@app.route("/numguess", methods=["get", "post"])
def numguess():
    res = ""
    # もしセッション情報の中に乱数がセットされていなかった場合
    if ("rnum" not in session):
        # セッション情報に乱数を格納し
        session["rnum"] = random.randint(1, 100)
        # セッション情報のカウントを0に初期化する
        session["count"] = 0
    # もしリクエストメソッドがPOSTで、かつnumが送信されていた場合
    if (request.method == "POST" and "num" in request.form):
        try:
            # numを取得
            num = int(request.form["num"])
            # 乱数を取得
            rnum = session["rnum"]
            # カウントを取得
            count = session.get("count")
            # カウントアップ
            count += 1
            # カウントをセッション情報に格納
            session["count"] = count
            # 試行回数を出力
            res = str(count) + "tries, " + str(num) + ": "
            # もしnumが乱数より小さかった場合
            if (num < rnum):
                # small!と出力
                res += "small!"
            # もしnumが乱数より大きかった場合
            elif (num > rnum):
                # big!と出力
                res += "big!"
            # それ以外（numが乱数と一致した場合）
            else:
                # Congratulationsと出力
                res += "Congratulations!"
                # セッション情報から乱数を削除
                session.pop("rnum")
                # セッション情報からカウントを削除
                session.pop("count")
        except:
            res = "error"
    # 結果をクライアントに返す
    return render_template("sample3.html", res=res)

app.secret_key = "がっこうぐらし！"
app.run(host="0.0.0.0", port=8000)
