# The planner
## Uma agenda simples feita com Flask e um pouco de SQLAlchemy

Projeto da disciplina de Engenharia de Software (Prof. César Olavo).

Equipe: Tiago de Tarso, Israel Leite, Rafael Pinheiro, Ruann Yury

<b>3: Diagrama de Caso de Uso</b> 


![alt text](https://i.ibb.co/xMW0TCM/Diagrama-de-caso-de-uso.png)

1 - Servidor busca usuário no sistema, se não houver, requisita seu cadastro

2 - Com o usuário logado ou registrado é possível criar e/ou editar os contatos (CRUD)

3 - Fazer logout


<b>Diagrama de Estado (CRUD)</b>

CREATE:

![alt text](https://i.ibb.co/N2c7HTX/adicionarcontatos.png)

READ:

![alt text](https://i.ibb.co/myWzxn5/mostracontatos.png)

UPDATE:

![alt text](https://i.ibb.co/tmyz24X/atualizarcontatos.png)

DELETE:

![alt text](https://i.ibb.co/2yVxC8P/deletarcontatos.png)

<b>Diagramas de Atividade</b>
 
Navegação de Telas e Login: 

![alt text](https://i.ibb.co/DKJdwcH/diagramaatividade.png)

Listagem de Contatos

![alt text](https://i.ibb.co/QjtqqXt/atividadelistarcontatos.png)

<b>Diagrama de Classes</b>

![alt text](https://i.ibb.co/25G4grV/classeumlfinal.png)

<b>Diagrama de Estado de um objeto Usuário</b>

![alt text](https://i.ibb.co/S3pjzzD/diagramadeestado.png)

<b>Diagrama de Componentes</b>

![alt text](https://i.ibb.co/9rWkm7s/Diagrama-de-componentes.png)

Padrão utilizado: MVC, pastas divididas entre models (com banco de dados e JSON), views (templates com html) e controllers (auth.py)

<b>Diagrama de Implantação</b>

![alt text](https://i.ibb.co/0m36CNM/Diagrama-de-implanta-o.png)

<h3>Ferramentas</h3>
Online Visual Paradigm - https://online.visual-paradigm.com/

LucidChart - https://www.lucidchart.com/pages/pt/exemplos/fluxograma-online

Figma - https://www.figma.com

Frameworks e bibliotecas - <a href="https://github.com/ruannyury/Agenda/blob/main/requirements.txt">Requirements</a>

<b>Design Patterns</b>

Factories - Criação das classes (<a href="https://github.com/ruannyury/Agenda/blob/main/app/models/models.py">Models</a>) e dos objetos (<a href="https://github.com/ruannyury/Agenda/blob/main/app/auth.py">Auth</a>, linha 78, e em <a href="https://github.com/ruannyury/Agenda/blob/main/app/views.py">Views</a>, linhas 88, 115 e 133)

Observer - <a href="https://flask-login.readthedocs.io/en/latest/#custom-login-using-request-loader">Implementado com Flask Login</a>

<h3>Referências</h3>
Documentação do Python - https://docs.python.org/pt-br/3/tutorial/index.html

Curso de UML - Unified Modeling Language - https://www.youtube.com/playlist?list=PLucm8g_ezqNqCRGHGHoacCo6N1bfN7hXZ

Documentação do SQLAlchemy- https://docs.sqlalchemy.org/en/14/

Documentação do Flask Login - https://flask-login.readthedocs.io/en/latest/

Curso de Flask - Júlia Rizza - https://youtube.com/playlist?list=PL3BqW_m3m6a05ALSBW02qDXmfDKIip2KX

Projeto Criptocurrency - Ruann Yury e Israel Leite - https://github.com/ruannyury/cryptocurrency
