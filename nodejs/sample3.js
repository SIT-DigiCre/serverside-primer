var express = require("express");
var session = require("express-session");
var bodyParser = require("body-parser");
var app = express();

HTMLHEAD = `
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <title>Guess Number</title>
        <meta content="text/html; charset=utf-8" http-equiv="content-type" />
        <meta content="width=device-width, initial-scale=1" name="viewport" />
    </head>
    <body>
        <form action="" method="post">
`
HTMLFOOT = `
            <p>Input Your Guess: <input type="text" name="num" /></p>
            <p><input type="submit" /></p>
        </form>
    </body>
`

app.use(bodyParser.urlencoded({extended: true}));
app.use(session({
    secret: "がっこうぐらし！",
    resave: false,
    saveUninitialized: true
}));

app.get("/numguess", (req, res) => {
    res.status(200).send(HTMLHEAD + HTMLFOOT);
});

app.post("/numguess", (req, res) => {
    if (req.session.rnum === undefined) {
        req.session.rnum = Math.floor(Math.random() * 100) + 1;
        req.session.count = 0;
    }
    out = "";
    if (req.body !== undefined && req.body.num !== undefined) {
        num = parseInt(req.body.num);
        rnum = parseInt(req.session.rnum);
        count = parseInt(req.session.count);
        count += 1;
        req.session.count = count;
        out += "<p>";
        if (num !== NaN && rnum !== NaN) {
            out += count + "tries, " + num + ": ";
            if (num < rnum) {
                out += "small!";
            } else if (num > rnum) {
                out += "big!";
            } else if (num == rnum) {
                out += "Congratulations!";
                delete req.session.rnum;
                delete req.session.count;
            }
        } else {
            out += "error";
        }
        out += "</p>";
    }
    res.status(200).send(HTMLHEAD + out + HTMLFOOT);
});

app.listen(8000);
