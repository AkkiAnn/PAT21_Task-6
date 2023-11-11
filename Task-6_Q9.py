def find_triplet_with_sum(nums, target):
    n = len(nums)
# Sort list 
    nums.sort()
    for i in range(n - 2):
        left = i + 1
        right = n - 1
    while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum == target:
                return [nums[i], nums[left], nums[right]]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
# Return none if no such triplet found
    return None  
# Example 
my_list = [10, 20, 30, 9]
target_value = 59
triplet = find_triplet_with_sum(my_list, target_value)
if triplet is not None:
    print("Triplet with sum", target_value, ":", triplet)
else:
    print("No such triplet found.")
