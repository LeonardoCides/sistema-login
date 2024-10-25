# todas as funcoes do projeto
import sys
import time 

def menu():
    print("-"*20)
    print("1- Entrar com login\n"+
    "2- Criar uma conta\n"+
    "3- Sair")
    print("-"*20)

#-----------------------------------------------------------------

dados_usuario = {}

def cadastrar_usuario(nome,cpf, idade, senha):
    if (verifica_idade(idade)):
        verificar_cpf(cpf)
        nome_valido(nome)
        confirmar_senha(senha)
        dados_usuario[nome] = {'senha':senha, 'idade': idade, 'cpf': cpf} 
        print('Cadastrando usuario...')
        time.sleep(2)
        print("Cadastrado com sucessor!")
    else:
        print("Usuario menor de idade")
    print(dados_usuario)
    
def verificar_cpf(cpf):
    for i in dados_usuario.values():
        if cpf in i.values():
            print("Já existe uma conta cadastrada com este CPF!")
            sys.exit()
        else:
            continue
        
def nome_valido(nome):
    if nome not in dados_usuario:
        verificacao = True
        while verificacao:
            if(len(nome) > 4):
                verificacao = False
                continue
            else:
                print('Nome deve conter mais de 4 caracteres')
                verificacao = True
                nome = str(input("Informe seu nome: "))
    else:
        print("Ja existe este nome cadastrado, utilize outro!!!")
        sys.exit()

def verifica_idade(idade):
    if idade >= 18:
        return True
    else:
        return False
        
def confirmar_senha(senha):
    if(len(senha)>6):
        if("@"and "#" and "!" not in senha):
           print("A senha deve conter pelo menos 2 caracteres especiais!")
           sys.exit() 
        else:
            testar_senha = True
            while testar_senha:
                confirmar_senha = str(input("Confirme sua senha novamente: "))
                if (senha == confirmar_senha):
                    print("Senha salva com sucesso!")
                    testar_senha = False
                else:
                    print("As senhas nao coecidem")
                    testar_senha = True 
    else:
        print("Senha deve ter mais de 7 digitos.")
        sys.exit()

#-----------------------------------------------------------------

def login(nome, senha):
    if nome in dados_usuario.keys():
        if senha in dados_usuario[nome]['senha']:
            print("Entrando na sua conta...")
            time.sleep(3)
            print('Voce fez login na sua conta, divirta-se!')
            sys.exit()
        else:
            print('Sua senha esta incorreta!')
    else:
        print('Nenhuma conta foi encontrada! Faca o registro e entre na sua conta!')

#-----------------------------------------------------------------

def deletar_usuario(nome,senha):
    if nome in dados_usuario.keys():
        if senha in dados_usuario[nome]['senha']:
            dados_usuario.pop(nome)
    print(dados_usuario)
                
