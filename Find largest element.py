def find_largest(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest
print(find_largest([10, 5, 8, 15, 32])) #Output should be 32