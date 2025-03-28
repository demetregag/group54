def sum_of_positives(arr):
    return sum(num for num in arr if num > 0)

# Example usage
print(sum_of_positives([1, -4, 7, 12]))  # Output: 20
