def count_sheeps(sheep):
    return sheep.count(True)

# ტესტი
sheep_array = [True,  True,  True,  False,
               True,  True,  True,  True,
               True,  False, True,  False,
               True,  False, False, True,
               True,  True,  True,  True,
               False, False, True,  True]

print(count_sheeps(sheep_array))  # Output: 17
