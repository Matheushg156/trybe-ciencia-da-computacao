# Dada uma lista, descubra o menor elemento.
# Por exemplo, [5, 9, 3, 19, 70, 8, 100, 2, 35, 27] deve retornar 2.


def smallest(numbers):
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest


print(smallest([5, 9, 3, 19, 70, 8, 100, 2, 35, 27]))

# Usando a função min()


def smallest(numbers):
    return min(numbers)


print(smallest([5, 9, 3, 19, 70, 8, 100, 2, 35, 27]))
