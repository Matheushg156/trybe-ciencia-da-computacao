""" O Fatorial de um número inteiro é representado pela multiplicação
de todos os números predecessores maiores que 0. Por exemplo, o
fatorial de 5 é 120 pois 5! = 1 * 2 * 3 * 4 * 5. """
""" Escreva um código que calcule o fatorial de um número inteiro. """

number = 5
result = 1

for factor in range(1, number + 1):
    result *= factor
print(result)
