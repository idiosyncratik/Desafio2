# Faça um código para ler 5 nomes de usuários e suas respectivas senhas, e
# armazenar cada lista em um array diferente, após completar a digitação,
# imprimir , nome, senha e posição dos dados no array
# Altere o sistema anterior e faça um sistema de login, pedindo a senha do usuário e
# mostrando seu nome e a mensagem, login efetuado com sucesso.
# dê apenas três tentativas de login, após digitar o nome ou senha errada 3 vezes o
# sistema encerra
nomes = []
senhas = []

for i in range(5):
    nome = input("Digite seu nome de usuário: ")
    senha = input(f"Digite a senha para {nome}: ")

    nomes += [nome]
    senhas += [senha]

tentativas = 3
while tentativas > 0:
    nome_login = input("Digite o seu login: ")
    senha_login = input("Digite a sua senha: ")

    for i in range(5):
        if nomes[i] == nome_login and senhas[i] == senha_login:
            print("Login efetuado com sucesso.")
            tentativas = 0
            break
    else:
        print("Nome de usuário ou senha incorretos. Tente novamente.")

    tentativas -= 1

if tentativas == 0:
    print("Três tentativas de login incorretas. O sistema foi encerrado.")
