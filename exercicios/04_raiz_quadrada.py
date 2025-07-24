#Faça um programa que receba um número inteiro e calcule sua raiz quadrada e exiba o resultado.

numero = input("Entre com um número para calcular a sua raiz quadrada: ")
numero = int(numero)

raiz = numero ** (1/2) # numerpo ** 05
print("Raiz quadra de ", numero, "é: ", raiz)