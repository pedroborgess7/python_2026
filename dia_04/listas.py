# %%

# Uma maneira de definir listas
idades = [28, 42,43, 35,39, 28,38]
print(idades)

# %%
Pedro = ["Téo", "Calvo", 32, True, "Casado", 2342.98]
print(Pedro)

# %%
type(Pedro)

# %%

# idade
print(Pedro[2])

# renda
print(Pedro[5])

print(Pedro[0])

# %%

idades = [28, 42,43, 35,39, 28,38, 42, 34]

soma = sum(idades)
print("soma idades:", soma)

print("qtde idades:", len(idades))

print("media idades:", soma/len(idades))

print("menor idade:", min(idades))

print("maior idade:", max(idades))

# %%

Pedro = ["Pedro Borges",
       32,
       True,
       "Solteiro",
       ["estagiario", "ds jr.", "ds pl", "ds sr.", "head"],
       [1500, 4000, 4550, 6500, 10000],
       ["Ana", "Maria", "Claudia"]]

print("Tamanho de téo:", len(Pedro))

print(Pedro[6][0])

exs = Pedro[6]
primeira_ex = exs[0]
print(primeira_ex)

# %%

tamanho = len(Pedro)
pos = tamanho - 1

exs = Pedro[pos]
Pedro[pos][len(exs) - 1]

# %%

Pedro[-1][-1]

# %%

# primeiros 4 elementos
Pedro[0:4]

# %%

Pedro[4][3:5]

# %%
print(Pedro[4][3:])
print(Pedro[4][-2:])

# %%
# primeiros 4 elementos
Pedro[:4]

# %%
# Pedro[ start : stop ]

# %%

salarios = Pedro[5]
salarios[::2]

# Pedro[ start : stop : step ]