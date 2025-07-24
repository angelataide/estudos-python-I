#Faça um programa que vende uma garrada de água:
#Se o cliente escolher água mineral natural, será cobrado R$1,50
#Se o cliente escolher água mineral com gás, será cobrado R$2,50

texto = """Escolha a sua água para comprar
(1) Água mineral natural
(2) Água mineral com gás
"""

opcao = input(texto)

valor_item = 0
if opcao == "1":
    valor_item = 1.5
elif opcao == "2":
    valor_item = 2.5
else:
    print("Entre com a opção correta, por favor.")
    
qtde = input("Quantas garrafas? ")
qtde = int(qtde)
valor_total = valor_item * qtde
print("Sua conta deu: R$", valor_total)