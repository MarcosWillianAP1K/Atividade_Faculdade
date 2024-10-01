import pandas as apelido


banco_de_dados = {
    "nomes": ["raildon", "joao marcos", "hermeson", "marcos"],
    "idade" : [35, 46, 35, 65]
}

df = apelido.DataFrame(banco_de_dados)

print(df)

print(df[df['idade'] > 40])

print(df.loc[1])

df.columns = df.columns.str.upper().str.replace(" ", "_").str.replace("\w", "",regex=True)

print(df)