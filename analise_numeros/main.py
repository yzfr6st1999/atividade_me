def analisar_lista(numeros):
    soma = sum(numeros)
    quantidade = len(numeros)
    media = round(soma / quantidade, 2)
    maior = max(numeros)
    menor = min(numeros)
    quantidade_pares = sum(1 for num in numeros if num % 2 == 0)

    return {
        "media": media,
        "maior": maior,
        "menor": menor,
        "quantidade_pares": quantidade_pares
    }
