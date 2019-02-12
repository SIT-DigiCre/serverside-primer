var express = require("express");
var app = express();

HTMLHEAD = `
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <title>Welcome</title>
        <meta content="text/html; charset=utf-8" http-equiv="content-type" />
        <meta content="width=device-width, initial-scale=1" name="viewport" />
    </head>
    <body>
        <form action="" method="get">
`
HTMLFOOT = `
            <p>Input Your Name: <input type="text" name="name" /></p>
            <p><input type="submit" /></p>
        </form>
    </body>
`

app.get("/", (req, res) => {
    if (req.query.name !== undefined && req.query.name.length > 0) grt = "<h1>Hello, " + req.query.name + ".</h1>";
    else grt = "<h1>Welcome, anonymous.</h1>";
    res.status(200).send(HTMLHEAD + grt + HTMLFOOT);
});

app.listen(8800);
