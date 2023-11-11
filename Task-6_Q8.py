def minimum_element(sorted_list):
    if not sorted_list:
# Handle the case of an empty list
        return None  
    return sorted_list[0]
# Example 
sorted_list = [1, 2, 3, 4, 5, 6, 7]
min_element = minimum_element(sorted_list)
if min_element is not None:
    print("Minimum element:", min_element)
else:
    print("The list is empty.")
