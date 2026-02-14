
 # %%

lista = [2, 132, "pedro", ["ds", "de", "da"], True]

lista[2]

# %%

# pares de chave/valor

dados_pedro = {
    "sobrenome":"Borges",
    "nome":"pedro", 
    "filhos":True,
    "formacao":["estatística", "bigdata datascience"],
    "cargos":[
        {"nome": "ds jr.", "empresa": "tapps"},
        {"nome": "ds pl.", "empresa": "sas" },
        {"nome": "ds sr.", "empresa": "boticario"},
        {"nome": "ds espec.", "empresa": "via varejo"},
    ]
}

# %%
print(dados_pedro)
print(dados_pedro["formacao"][-1])
print(dados_pedro["cargos"][-1]["empresa"])

# %%
dados_pedro["estado civil"] = "casado"

# %%

print("Chaves:", dados_pedro.keys())
print("Valores:", dados_pedro.values())
print("Items:", dados_pedro.items())

# %%

for i in [10,20,45,28,"pedro"]:
    print(i)

# %%

for i in dados_pedro:
    print(i, "->", dados_pedro[i])

# %%

for chave, valor in dados_pedro.items():
    print(chave, "->", valor)

# %%

dados_pedro["estado civil"] = "solteiro"
dados_pedro["fodase"] = None
# %%
dados_pedro