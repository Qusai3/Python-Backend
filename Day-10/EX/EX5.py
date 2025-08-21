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

prime_gen = primes()  
for _ in range(6):    
    print(next(prime_gen), end=" ")
print()