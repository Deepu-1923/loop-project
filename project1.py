def print_positive_numbers(numbers):
    positive_numbers = [num for num in numbers if num > 0]
    print("Output:", ', '.join(map(str, positive_numbers)))
l1 = [12, -7, 5, 64, -14]
l2 = [12, 14, -95, 3]
print("Input: list1 =", l1)
print_positive_numbers(l1)
print("\nInput: list2 =", l2)
print_positive_numbers(l2)
