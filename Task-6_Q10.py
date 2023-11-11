def has_sublist_with_sum_zero(nums):
    cumulative_sum = 0
    sum_set = set()
    for num in nums:
        cumulative_sum += num
        if cumulative_sum == 0 or cumulative_sum in sum_set:
            return True
        sum_set.add(cumulative_sum)
    return False
# Example 
my_list = [4, 2, -3, 1, 6]
result = has_sublist_with_sum_zero(my_list)
if result:
    print("There is a sub-list with a sum equal to zero.")
else:
    print("No sub-list with a sum equal to zero found.")
