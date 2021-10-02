
numbers = range(100000000)


def is_even(number):
    return number % 2 == 0


even_numbers = list(filter(is_even, numbers))
print(sum(even_numbers))
