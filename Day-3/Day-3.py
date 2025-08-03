#day 3 ex

import math
import statistics

numbers_input = input("Enter numbers:  ")


numbers = numbers_input.split()
numbers = [float(n) for n in numbers]

mean = statistics.mean(numbers)
median = statistics.median(numbers)
mode = statistics.mode(numbers)

sqrt_f= math.sqrt(numbers[0])

print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)
print("SQRT",round(sqrt_f,2))
