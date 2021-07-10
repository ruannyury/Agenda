addressbook = {
    "ruann yury": [
        {
            "nome": "Israel",
            "idade": "18"
        }, {
            "nome": "Rafael",
            "idade": "19"
        }
    ],
    "israel leite": [
        {
            "nome": "Ruann",
            "idade": "19"
        }, {
            "nome": "Rafael",
            "idade": "19"
        }
    ],
    "rafael pinheiro": [
        {
            "nome": "Ruann",
            "idade": "19"
        }, {
            "nome": "Israel",
            "idade": "19"
        }
    ]
}

nome = input('Nome completo do usuário: ')

posicao = 0
for contatos in addressbook[nome]:
    posicao += 1
    print(f'{contatos["nome"]} {contatos["idade"]}')
