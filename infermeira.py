import webbrowser
import os

linha = ('-' * 67)
vazio = ' '

while True:
    print(linha)
    print('Olá me chamo ana e sou sua enfermeira digital'.center(67))
    print(linha)
    print(vazio)
    dor = str(input('Digite aqui o que você está sentindo: '))
    pesquisar = ('https://www.google.com.br/search?q=')
    pesquisa = (pesquisar + dor) 
    webbrowser.open(pesquisa)
    print(vazio)
    print(linha)
    opção = str(input('Digite [S] se tem mais alguma pergunta ou digite [N] para encerrar: ')).upper()
    os.system('clear') or None
    if opção == 'N':
        print('Obrigado ! E volte sempre que precisar'.center(67))
        break