<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <title>Welcome</title>
        <meta content="text/html; charset=utf-8" http-equiv="content-type" />
        <meta content="width=device-width, initial-scale=1" name="viewport" />
    </head>
    <body>
	  <form action="" method="get">
            <h1>
            <?php
            if (isset($_GET["name"]) && strlen($_GET["name"]) > 0) print("Hello, ".$_GET["name"].".");
            else print("Welcome, anonymous.")
            ?>
            </h1>
            <p>Input Your Name: <input type="text" name="name" /></p>
            <p><input type="submit" /></p>
        </form>
    </body>
</html>
