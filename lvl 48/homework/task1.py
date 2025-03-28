def opposite(number):
    return -number

def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

def simple_multiplication(number):
    return number * 8 if number % 2 == 0 else number * 9

def abbrev_name(name):
    return ".".join([n[0] for n in name.upper().split()])

def find_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

def invert(lst):
    return [-x for x in lst]

def position(alphabet):
    return f"Position of alphabet: {ord(alphabet) - 96}"

def smash(words):
    return " ".join(words)

def grow(arr):
    result = 1
    for num in arr:
        result *= num
    return result

def hero(bullets, dragons):
    return bullets >= dragons * 2
