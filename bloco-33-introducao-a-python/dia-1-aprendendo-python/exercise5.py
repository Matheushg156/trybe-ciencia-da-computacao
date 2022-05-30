# Calcule a média aritmética dos valores contidos em uma lista.


def average(list):
    sum = 0
    for number in list:
        sum += number
    return sum / len(list)
