def soma(a:float, b:float, c:float)->float:
    return a + b + c

def media(a:float, b:float, c:float)->float:
    return soma(a,b,c) / 3

a = float(input("entre com o valor de a: "))
b = float(input("entre com o valor de b: "))
c = float(input("entre com o valor de c: "))

print("Média:", media(a,b,c))