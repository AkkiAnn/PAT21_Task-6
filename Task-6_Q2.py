def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True
original_list = [10, 501, 22, 37, 100, 999, 87, 351]
prime_numbers = [num for num in original_list if is_prime(num)]
print("Prime numbers:", prime_numbers)
