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

app.get("/countup", (req, res) => {
    if (req.session.count === undefined) {
        req.session.count = 0;
    } else {
        req.session.count++;
    }
    res.status(200).render("sample2.ejs", { count: String(req.session.count) });
});

app.post("/countup", (req, res) => {
    req.session.count = 0;
    res.status(200).render("sample2.ejs", { count: String(req.session.count) });
});

app.listen(8000);
