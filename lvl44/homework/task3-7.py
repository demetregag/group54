# 3) Basic Mathematical Operations
def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        return value1 / value2

# 4) Remove String Spaces
def no_space(x):
    return x.replace(" ", "")

# 5) Convert a Boolean to a String
def boolean_to_string(b):
    return str(b)

# 6) Even or Odd
def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

# 7) Vowel Count
def get_count(sentence):
    return sum(1 for char in sentence if char in 'aeiouAEIOU')
