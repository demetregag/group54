

def find_minimum(user_list):
    minimum = user_list[0]  # პირველ ელემენტს ვანიჭებთ მინიმალურ მნიშვნელობად
    for num in user_list:
        if num < minimum:
            minimum = num
    print(minimum)


find_minimum([5, 3, 8, 1, 2])
find_minimum([12, 4, 6, 9, 10])
find_minimum([100, 50, 60, 40, 30])
find_minimum([7, 2, 5, 1, 8])
find_minimum([20, 15, 10, 5, 25])