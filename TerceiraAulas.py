#INPUTS
Usuario = input("Digite seu nome: ")
Email = input("Digite seu email: ")
Password = int(input("Digite sua senha: "))

if Email[Email.find("@"):] == "gmail.com":
    print("Seu email e valido")
else:
    Email = input("ERRO, Digite seu email gmail: ")
#LISTAS
