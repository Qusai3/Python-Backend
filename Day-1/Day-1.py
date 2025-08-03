#day 1 ex
num = int(input("Enter num: "))

if num <= 1:
    print("Not a prime num")
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print("Not a prime num")
            break
    else:
        print("its Prime number")