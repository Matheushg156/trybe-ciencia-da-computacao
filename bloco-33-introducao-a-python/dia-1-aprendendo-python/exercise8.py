# Considere que a cobertura da tinta é de 1 litro para
# cada 3 metros quadrados e que a tinta é vendida em latas
# de 18 litros, que custam R$ 80,00. Crie uma função que
# retorne dois valores em uma tupla contendo a quantidade
# de latas de tinta a serem compradas e o preço total a
# partir do tamanho de uma parede(em m²).


def calculate_tinta(meters):
    preco = 80
    litros = meters / 3
    latas = litros // 18
    if litros % 18:
        latas += 1
    return latas, latas * preco


print(calculate_tinta(60))
