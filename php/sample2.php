<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <title>Guess Number</title>
        <meta content="text/html; charset=utf-8" http-equiv="content-type" />
        <meta content="width=device-width, initial-scale=1" name="viewport" />
    </head>
    <body>
	    <form action="" method="post">
            <?php
            session_start();
            if (!isset($_SESSION["rnum"])) {
                $_SESSION["rnum"] = rand(1, 100);
                $_SESSION["count"] = 0;
            }
            if (isset($_POST["num"])) {
                print("<p>");
                $num = $_POST["num"];
                $rnum = $_SESSION["rnum"];
                $count = $_SESSION["count"];
                if (is_numeric($num) && is_numeric($rnum) && is_numeric($count)) {
                    $count += 1;
                    $_SESSION["count"] = $count;
                    print($count."tries, ".$num.": ");
                    if ($num < $rnum) {
                        print("small!");
                    } else if ($num > $rnum) {
                        print("big!");
                    } else {
                        print("Congratulations!");
                        unset($_SESSION["rnum"]);
                        unset($_SESSION["count"]);
                    }
                } else print("error");
                print("</p>");
            }
            ?>
            <p>Input Your Guess: <input type="text" name="num" /></p>
            <p><input type="submit" /></p>
        </form>
    </body>
</html>
