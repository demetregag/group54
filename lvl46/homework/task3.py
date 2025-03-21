immutable_tuple = (1, 2, 3, 4, 5)

# Trying to modify an element (this will cause an error)
try:
    immutable_tuple[1] = 100
except TypeError as e:
    print("Error:", e)
