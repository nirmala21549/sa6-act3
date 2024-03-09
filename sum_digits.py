sum_of_digits = lambda num: sum(int(digit) for digit in str(num) if digit.isdigit())

number = 21549
print("Number:", number)
print("Sum of digits:", sum_of_digits(number))
