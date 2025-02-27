#INPUTS

##Usuario = input("Digite seu nome: ")
##Email = input("Digite seu email: ")
##Password = int(input("Digite sua senha: "))
##
##if Email[Email.find("@"):] == "gmail.com":
##    print("Seu email e valido")
##else:
##    Email = input("ERRO, Digite seu email gmail: ")

#Arrays-mercado

##custo = 405
##vendas = [108,193,10,25,30,99,105,203,12]
##
##print(f"o total de vendas foram de: {len(vendas)}")
##print(f"as vendas foi de {sum(vendas)} e o lucro: ",sum(vendas) - custo)
##
##print(f"o maior valor obitido foi o: {max(vendas)}")
##print(f"o menor valor obitido foi o: {min(vendas)}")
##
##print(f"essa foi a primeira venda: {vendas[0]}")
##
#Arrays-objects
produtos = ["macbookM1","GalaxS23","PCgamer","FoneHyperex","RedragonA"]
miura = ["sport","sport","sport","sport","saga"]

print(f"o macbookM1 existe: {"macbookM1" in produtos}")

print(produtos)
produtos.pop(1) #remove pelo indice
produtos.append("macbookM2")
produtos.remove("macbookM1")
print(produtos)
produtos[-2] = "RedragonB"
print(miura.count("sport"))
print(f"ordenada| alfabetica/cresente:{produtos.sort()},Contrario/decrasente:{produtos.sort(reverse=true)}")
