def find_maximum(numbers, compare):
    maximum = numbers[0]
    for num in numbers[1:]:
        if compare(num, maximum) > 0:
            maximum = num  
    return maximum
numbers = [123, 71, 215, 90, 0]
compare_function = lambda x, y: x - y  
maximum = find_maximum(numbers, compare_function)
print("Maximum number:", maximum)
