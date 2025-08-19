def prime_generator():
    num = 2   
    while True:   

        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):  
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            yield num   

        num += 1   



gen = prime_generator()  
for _ in range(10):      
    print(next(gen))  