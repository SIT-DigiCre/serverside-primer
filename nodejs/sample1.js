const express = require("express");
const app = express();
app.set('view engine', 'ejs');

app.get("/", (req, res) => {
    if (req.query.name !== undefined && req.query.name.length > 0) grt = "Hello, " + req.query.name + ".";
    else grt = "Welcome, anonymous.";
    res.status(200).render("sample1.ejs", { greetings: grt });
});

app.listen(8000);
