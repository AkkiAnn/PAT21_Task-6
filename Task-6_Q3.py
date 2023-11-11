def is_happy_number(n):
    def get_next(n):
        total = 0
        while n > 0:
            digit = n % 10
            total += digit ** 2
            n //= 10
        return total
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = get_next(n)
    return n == 1
def count_happy_numbers(numbers):
    count = 0
    for n in numbers:
        if is_happy_number(n):
            count += 1
    return count
# Given 
numbers = [10, 501, 22, 37, 100, 999, 87, 351]
happy_count = count_happy_numbers(numbers)
print("Number of happy numbers in the list:", happy_count)
