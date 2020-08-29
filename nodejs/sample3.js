var express = require("express");
var session = require("express-session");
var bodyParser = require("body-parser");
var app = express();

HTMLHEAD = `
`

app.use(bodyParser.urlencoded({extended: true}));
app.use(session({
    secret: "がっこうぐらし！",
    resave: false,
    saveUninitialized: true
}));

app.get("/numguess", (req, res) => {
    res.status(200).render("sample3.ejs", { res: "" });;
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
    }
    res.status(200).render("sample3.ejs", { res: out });;
});

app.listen(8000);
