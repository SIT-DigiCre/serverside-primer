<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <title>Access counter</title>
        <meta content="text/html; charset=utf-8" http-equiv="content-type" />
        <meta content="width=device-width, initial-scale=1" name="viewport" />
    </head>
    <body>
        <form action="" method="post">
            <?php
            session_start();
            if (!isset($_SESSION["count"]) || $_SERVER["REQUEST_METHOD"] === "POST") {
                $_SESSION["count"] = 0;
            } else {
                $_SESSION["count"]++;
            }
            print("<p>");
            print($_SESSION["count"]);
            print("</p>");
            ?>
            <p><input type="submit" value="reset" /></p>
        </form>
    </body>
</html>
