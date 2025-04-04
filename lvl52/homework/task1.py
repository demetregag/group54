def find_smallest_int(arr):
    return min(arr)

def no_space(x):
    return x.replace(" ", "")

def check(seq, elem):
    return elem in seq

def string_to_array(s):
    return s.split(" ")

def make_negative(number):
    return -abs(number)

def check_for_factor(base, factor):
    return base % factor == 0

def string_to_number(s):
    return int(s)

def count_sheep(n):
    return ''.join(f"{i} sheep..." for i in range(1, n + 1))

def remove_nb(n):
    total = n * (n + 1) // 2
    result = []

    for a in range(1, n + 1):
        b = (total - a) / (a + 1)
        if b.is_integer() and b <= n:
            result.append((a, int(b)))
    
    return result


def get_grade(s1, s2, s3):
    avg = (s1 + s2 + s3) / 3
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    else:
        return 'F'

def name_shuffler(name):
    return ' '.join(name.split()[::-1])
