# Python code​​​​​​‌‌‌‌‌​‌‌‌​‌‌​‌​​‌​‌‌‌​​​‌ below
# Use print("messages...") to debug your solution.

def allPrimesUpTo(num):
    primes = []

    for number in range(2, num):
        is_prime = True

        for factor in range(2, int(number ** 0.5) + 1):
            if number % factor == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(number)

    return primes


print(allPrimesUpTo(10))  # [2, 3, 5, 7]
print(allPrimesUpTo(20))  # [2, 3, 5, 7, 11, 13, 17, 19]