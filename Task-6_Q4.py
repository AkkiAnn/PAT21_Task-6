def sum_of_first_and_last_digit(number):
# Convert number to string 
    number_str = str(number)
# Check number is negative and remove negative sign 
    if number_str[0] == '-':
        number_str = number_str[1:]
# first and last digits and convert to integers
    first_digit = int(number_str[0])
    last_digit = int(number_str[-1])
# Calculate sum of first and last digits
    total_sum = first_digit + last_digit
    return total_sum
# Input  
number = int(input("Enter an integer: "))
# Calculate and display the sum of first and last digit
result = sum_of_first_and_last_digit(number)
print("Sum of first and last digit:", result)