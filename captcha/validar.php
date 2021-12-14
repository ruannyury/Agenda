<?php
   session_start();
    if ($_POST["palavra"] == $_SESSION["palavra"]){
        echo "<h1>Voce Acertou</h1>";
        header("Location: http://127.0.0.1:5000/login");
        exit();
    }else{
        header("Location: http://127.0.0.1:5000");
        exit();
    }
?>