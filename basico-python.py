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

#Questão 1 lista simples que retorna numeros impare:
lista = [1, 2, 3, 4, 5, 6, 7]
resultado = retorna_impares(lista)
print(f"Na lista {lista}, este numeros são impares: {resultado}")  # Saída: [1, 3, 5, 7]

#Questão 2 - retorna a lista de primos
primos = filtrar_primos(lista)
print(f"Na lista {lista}, este numeros são primos: {primos}")  # Saída: [2, 3, 5, 7]

