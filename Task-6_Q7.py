def first_non_repeating_element(nums):
# Create dictionary to store count
    count_dict = {}
# Iterate the list 
    for num in nums:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
# first non-repeating element
    for num in nums:
        if count_dict[num] == 1:
            return num
# If no non-repeating element is found, return None
    return None
# Example 
my_list = [3, 5, 7, 3, 2, 5, 7, 8]
result = first_non_repeating_element(my_list)
if result is not None:
    print("First non-repeating element:", result)
else:
    print("No non-repeating elements found in the list.")


