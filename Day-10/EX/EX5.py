def primes():
    num = 2
    while True:
        # check prime
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
        num += 1

prime_gen = primes()  # Fixed variable name
for _ in range(6):    # Fixed loop variable
    print(next(prime_gen), end=" ")   # 2 3 5 7 11 13
print()