list1 = [1, 2, 3, 4, 5, 2, 6]
list2 = [2, 3, 4, 4, 5, 6, 7]
list3 = [3, 4, 5, 6, 7, 8, 9]
# Find duplicates in three lists 
common_duplicates = list(set(list1) & set(list2) & set(list3))
print("Common duplicates:", common_duplicates)
