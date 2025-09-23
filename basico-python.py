#Questão 1
def retorna_impares(numeros):
    return [n for n in numeros if n % 2 != 0]

#Questão 2
def numero_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filtrar_primos(numeros):
    return [n for n in numeros if numero_primo(n)]

#Questão 3
def diferenca_simetrica(lista1, lista2):
    return list(set(lista1) ^ set(lista2))

#Questão 4
def segundo_maior(lista):
    if len(lista) < 2:
        return None  # não existe segundo maior
    lista_unica = list(set(lista))  # remove duplicados
    lista_unica.sort(reverse=True)  # ordena em ordem decrescente
    if len(lista_unica) >= 2:
        return lista_unica[1]
    return None

#Questão 5
def ordenar_por_nome(pessoas):
    return sorted(pessoas, key=lambda pessoa: pessoa[0])

#Questão 1 lista simples que retorna numeros impare:
lista = [1, 2, 3, 4, 5, 6, 7]
n_Impar = retorna_impares(lista)
print(f"Na lista {lista}, este numeros são impares: {n_Impar}")  # Saída: [1, 3, 5, 7]

#Questão 2 - retorna a lista de primos
primos = filtrar_primos(lista)
print(f"Na lista {lista}, este numeros são primos: {primos}")  # Saída: [2, 3, 5, 7]

#Questão 3 - Apartir de duas listas, retorna a diferença simetrica
resultado = diferenca_simetrica(n_Impar, primos)
print(f"Nas listas {n_Impar} e {primos}, estes numeros não aparecem nas duas listas: {resultado}")  # Saída: [1, 2]

#Questão 4 - Retorna segundo maior valor da lista
resultado = segundo_maior(lista)
print(f"Na lista {lista}, este é o segundo maior valor da lista: {resultado}")  # Saída: 6

#Questão 5 - Ordenar tupla 
nome_Idade = [("Carlos", 25), ("Ana", 30), ("Bruno", 20), ("Gil", 45), ("Anakin", 22)]
resultado = ordenar_por_nome(nome_Idade)
print(f"A partir da Tupla {nome_Idade}, temos a tupla ordenada por alfabeto: {resultado}")