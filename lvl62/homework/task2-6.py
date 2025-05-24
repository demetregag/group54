
# 2
strings = ["apple", "banana", "cherry"]
uppercased = list(map(str.upper, strings))
print("Uppercased:", uppercased)
# 3
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print("Squared:", squared)
# 4
numbers_add = [10, 20, 30, 40]
added_five = list(map(lambda x: x + 5, numbers_add))
print("Add 5:", added_five)
# 5
celsius = [0, 20, 37, 100]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print("Fahrenheit:", fahrenheit)
# 6
words = ["hello", "world", "python", "map"]
first_chars = list(map(lambda word: word[0], words))
print("First characters:", first_chars)
