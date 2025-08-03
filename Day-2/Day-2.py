#day 2 ex
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


num = int(input("Enter a num: "))


if num < 0:
    print("Sorry, The nimber less than 0")
else:
    result = factorial(num)
    print("The factorial of", num, "is", result)