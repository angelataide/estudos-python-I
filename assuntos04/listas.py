# %%

idades = [28, 42, 43, 39, 28, 38]
print(idades)
# %%

teo = ["Téo", "Calvo", 32, 1, "Casado", 2342,98]
# %%

type(teo)

# %%

#idade
print(teo[2])

#renda
print(teo[5])

print(teo[0])

# %%

idades = [28, 42, 43, 35, 39, 28, 38]

print("soma idades:", sum(idades))

print("qtde idades:", len(idades))

print("media idades:", sum(idades)/len(idades))

print("menor idade:", min(idades))

print("maior idade:", max(idades))

# %%

teo = ["Téo Calvo", 32, True, "Casado", ["Ana", "Maria", "Claudia"]]

print(len(teo))

teo[4][0]

exs = teo[4]
primeira_ex = exs[0]
print(primeira_ex)

# %%

tamanho = len(teo)
pos = tamanho - 1
exs = teo[pos]

teo[pos][len(exs) -1]

# %%

teo[0:4]

# %%
