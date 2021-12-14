<!--
No campo src da tag img abaixo enviaremos 4 parametros via GET
l = largura da imagem
a = altura da imagem
tf = tamanho fonte das letras
ql = quantidade de letras do captcha
-->

<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <meta http-equiv="X-UA-Compatible" content="IE=edge">
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <title>Captcha</title>
   <link rel="stylesheet" href="styles/global.css">
   <link rel="stylesheet" href="styles/home.css">
   <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@700;900&family=Rokkitt:wght@600&display=swap" rel="stylesheet">

</head>

<body>
    
      <div class="wrapper">
         <img src="captcha.php?l=150&a=50&tf=20&ql=5" id="captcha">
            <form action="validar.php" name="form" method="post" id="captchaform">
               <div id="text">  
                  <input type="text" name="palavra" placeholder="Captcha aqui"><br>
               </div> 
                  <button type="submit" id="enviar">Validar Captcha</button>
            </form>
      </div>
   
</body>
</html>
