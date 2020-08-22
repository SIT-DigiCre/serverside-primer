var express = require("express");
var session = require("express-session");
var bodyParser = require("body-parser");
var app = express();

HTMLHEAD = `
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <title>Access counter</title>
        <meta content="text/html; charset=utf-8" http-equiv="content-type" />
        <meta content="width=device-width, initial-scale=1" name="viewport" />
    </head>
    <body>
        <form action="" method="post">
`
HTMLFOOT = `
            <p><input type="submit" value="reset" /></p>
        </form>
    </body>
`

app.use(bodyParser.urlencoded({extended: true}));
app.use(session({
    secret: "がっこうぐらし！",
    resave: false,
    saveUninitialized: true
}));

app.get("/countup", (req, res) => {
    if (req.session.count === undefined) {
        req.session.count = 0;
    } else {
        req.session.count++;
    }
    res.status(200).send(HTMLHEAD + "<p>" + String(req.session.count) + "</p>" + HTMLFOOT);
});

app.post("/", (req, res) => {
    req.session.count = 0;
    res.status(200).send(HTMLHEAD + "<p>" + String(req.session.count) + "</p>" + HTMLFOOT);
});

app.listen(8000);
