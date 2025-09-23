import numpy as np

def outliers_desvio_padrao(dados, n_std=3):
    media = np.mean(dados)
    desvio = np.std(dados)
    limite_inferior = media - n_std * desvio
    limite_superior = media + n_std * desvio
    outliers = [x for x in dados if x < limite_inferior or x > limite_superior]
    return outliers

#Questão 6 - Otiliers:
valores = [10, 12, 13, 11, 12, 100, 9, 11, 10]
print(outliers_desvio_padrao(valores, n_std=2))  
# Saída: [100]

#Questão 7 - Concatenado DataFrames
df1 = pd.DataFrame({
    "id": [1, 2],
    "nome": ["Amelia", "Luana"]
})

df2 = pd.DataFrame({
    "id": [3, 4],
    "idade": [25, 30]
})

df_linhas = pd.concat([df1, df2], axis=0) #completa com NaN
print(df_linhas)

df_colunas = pd.concat([df1, df2], axis=1) # Lado a lado
print(df_colunas)

#Questão 8 - Lendo arquivo csv

df = pd.read_csv("Exemplo.csv")

# Exibindo as primeiras linhas (por padrão, mostra 5)
print(df.head())

#Questão 9 - Filtrando colunas
df = pd.DataFrame({
    "nome": ["Ana", "Bruno", "Carlos", "Diana"],
    "idade": [23, 35, 19, 42],
    "cidade": ["SP", "RJ", "SP", "MG"]
})

# Selecionar apenas a coluna 'nome'
coluna_nomes = df["nome"]
print(coluna_nomes)

filtro_idade = df[df["idade"] > 30]
print(filtro_idade)

#Questão 10- valores ausentes
