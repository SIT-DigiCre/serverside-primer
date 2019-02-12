#!/usr/bin/env python3
from flask import Flask, request

app = Flask(__name__)
PORT = 8800
HTMLHEAD = """
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <title>Welcome</title>
        <meta content="text/html; charset=utf-8" http-equiv="content-type" />
        <meta content="width=device-width, initial-scale=1" name="viewport" />
    </head>
    <body>
        <form action="" method="get">
"""
HTMLFOOT = """
            <p>Input Your Name: <input type="text" name="name" /></p>
            <p><input type="submit" /></p>
        </form>
    </body>
</html>
"""

@app.route("/")
def numguess():
    if ("name" in request.args and len(request.args["name"]) > 0):
        return (HTMLHEAD + "<h1>Hello, " + request.args["name"] + ".</h1>" + HTMLFOOT)
    return (HTMLHEAD + "<h1>Welcome, anonymous.</h1>" + HTMLFOOT)

app.run(host = "0.0.0.0", port = 8800)