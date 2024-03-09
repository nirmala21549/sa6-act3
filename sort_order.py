strings = ["apple", "banana", "carrot", "dragon fruit", "grape", "kiwi", "lemon", "mango"]

sorted_strings = sorted(strings, key=lambda x: (len(x), x))

print("Sorted strings:", sorted_strings)