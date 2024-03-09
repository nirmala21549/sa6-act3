def intersection(list1, list2):
    intersection_list = list(filter(lambda x: x in list2, list1))  
    return intersection_list

list1 = [1, 2, 3, 4, 5]
list2 = [2, 1, 5, 4, 9]

result = intersection(list1, list2)
print("Intersection of the two lists:", result)
