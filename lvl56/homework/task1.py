# 1. Cats and Dogs
def owned_cat_and_dog(cat_years, dog_years):
    def calc_animal_years(human_years):
        if human_years == 1:
            return 15
        elif human_years == 2:
            return 24
        else:
            return 24 + (human_years - 2) * 4
    
    cat = 0
    while calc_animal_years(cat) < cat_years:
        cat += 1
    dog = 0
    while calc_animal_years(dog) < dog_years:
        dog += 1
    return [cat, dog]

# 2. Third Angle of a Triangle
def other_angle(a, b):
    return 180 - a - b

# 3. Convert to Binary
def to_binary(n):
    return int(bin(n)[2:])

# 4. Multiply Array Values and Filter Non-Numeric
def sum_mix(arr):
    return sum(int(x) for x in arr)

# 5. Sum without highest and lowest number
def sum_array(arr):
    if arr is None or len(arr) < 3:
        return 0
    return sum(arr) - max(arr) - min(arr)

# 6. Combine Strings
def concatenate_names(first, last):
    return f"{first} {last}"

# 7. Opposite Number
def opposite(number):
    return -number

# 8. Remove String Spaces
def no_space(x):
    return x.replace(' ', '')

# 9. Make Upper Case
def make_upper_case(s):
    return s.upper()
