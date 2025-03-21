def find_missing_letter(chars):
    for i in range(1, len(chars)):
        if ord(chars[i]) - ord(chars[i - 1]) != 1:
            return chr(ord(chars[i - 1]) + 1)
    return None  # In case no letter is missing

# Example:
# find_missing_letter(['a','b','c','e'])  --> 'd'

def summation(n):
    return sum(range(1, n + 1))

# Example:
# summation(8)  --> 36 (because 1+2+3+4+5+6+7+8 = 36)

def lovefunc(flower1, flower2):
    return (flower1 % 2) != (flower2 % 2)

# Example:
# lovefunc(1, 4)  --> True; lovefunc(2, 2)  --> False

def find_it(seq):
    for num in set(seq):
        if seq.count(num) % 2 != 0:
            return num
    return None

# Example:
# find_it([20, 1, 1, 2, 2])  --> 20

def digital_root(n):
    while n > 9:
        n = sum(int(d) for d in str(n))
    return n

# Example:
# digital_root(16)  --> 7 (because 1 + 6 = 7)

def find_smallest_int(arr):
    return min(arr)

# Example:
# find_smallest_int([34, 15, 88, 2])  --> 2

def sum_array(arr):
    if not arr:
        return 0
    return sum(arr)

# Example:
# sum_array([1, 2, 3, 4])  --> 10

def wave(people):
    return [
        people[:i] + people[i].upper() + people[i+1:]
        for i in range(len(people)) if people[i] != ' '
    ]

# Example:
# wave("hello")  --> ["Hello", "hEllo", "heLlo", "helLo", "hellO"]

def sort_array(source_array):
    # Extract and sort the odd numbers.
    odds = sorted(x for x in source_array if x % 2 != 0)
    result = []
    odd_index = 0
    for num in source_array:
        if num % 2 != 0:
            result.append(odds[odd_index])
            odd_index += 1
        else:
            result.append(num)
    return result

# Example:
# sort_array([5, 3, 2, 8, 1, 4])  --> [1, 3, 2, 8, 5, 4]

def square_sum(numbers):
    return sum(x * x for x in numbers)

# Example:
# square_sum([1, 2, 2])  --> 9 (because 1*1 + 2*2 + 2*2 = 9)

def solution(arr):
    if arr is None:
        return []
    return sorted(arr)

# Example:
# solution([1, 3, 2, 10, 5])  --> [1, 2, 3, 5, 10]

def digitize(n):
    return [int(d) for d in str(n)][::-1]

# Example:
# digitize(35231)  --> [1, 3, 2, 5, 3]
