from funcionalidades import *

print("\nBem vindo ao nosso sistema, informe o que deseja abaixo:")

while True:
    menu()
    escolha = int(input("--> "))
    if escolha == 1:
        nome_login = str(input('Digite seu nickname: '))
        senha_login = str(input('Digite sua senha: '))
        login(nome_login,senha_login)
    elif escolha == 2:
        print("Para se registrar em nosso sistema, informe os dados abaixo!\n")
        try:
            
            nome = str(input('Informe seu nickname: '))
            cpf = str(input("Informe seu cpf: "))
            idade = int(input("Idade: "))
            senha = str(input('Informe sua senha: '))
            cadastrar_usuario(nome,cpf,idade,senha)
        except:
            print('Informe os campos corretamente')
    elif escolha == 3:
        print("Ate a proxima!")
        break
