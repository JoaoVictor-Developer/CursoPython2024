#Usuario (OBS:trasformar em obj)
nome = "Usuario002"
idade = 12
email = "LiraDev@gmail.com"
login = "12ab45"
#Carro (OBS:trasformar em obj)
carro = "miura sport"
ano = 1979
cv = 130
#ProcurandoCoisasNoTexto
if (email.find("@")) == -1:
#O Find Só Indentifica A Posiçao Do Caracter NAO RETORNA VALORES BOLEANOS!!!
    print("Isso nao é um email valido")
else:
    print("Login Efetuado")
#primeiro tipo de textos personalizaveis
if email == "UsuAriO002@gMail.com":
    print("seu nome: {}, sua idade: {}".format(nome,idade))
#segundo tipo de textos personalizaveis
if carro == "miura sport":
    print(f"modelo: {carro},Ano: {ano}, Cavalos: {cv}")
#upper/maiuscula
email = email.upper()
print(email)
#minuscula/lower
email = email.lower()
print(email)