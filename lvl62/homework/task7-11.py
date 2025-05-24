# 7
numbers1 = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers1))
print("Odd numbers:", odd_numbers)
# 8
words = ["apple", "banana", "cherry", "date", "fig"]
long_words = list(filter(lambda word: len(word) > 5, words))
print("Words longer than 5 characters:", long_words)
# 9
numbers2 = [-10, -5, 0, 5, 10]
non_negative = list(filter(lambda x: x >= 0, numbers2))
print("Non-negative numbers:", non_negative)
# 10
names = ["Alice", "Bob", "Amanda", "Charlie", "Angela"]
names_starting_with_a = list(filter(lambda name: name.startswith('A'), names))
print("Names starting with 'A':", names_starting_with_a)
# 11
numbers3 = [3, 5, 6, 9, 10, 12, 14]
divisible_by_3 = list(filter(lambda x: x % 3 == 0, numbers3))
print("Numbers divisible by 3:", divisible_by_3)