def sum_even_numbers(numbers):
    return sum(num for num in numbers if num % 2 == 0)

# მაგალითი:
numbers = [1, 2, 3, 4, 5, 6]
print(sum_even_numbers(numbers))  # Output: 12
