original_list = [10, 501, 22, 37, 100, 999, 87, 351]
#Separate even and odd numbers using list comprehensions
even_numbers = [num for num in original_list if num % 2 == 0]
odd_numbers = [num for num in original_list if num % 2 != 0]
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
