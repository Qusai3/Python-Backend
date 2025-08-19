def alternating_signs(numbers):
    sign = 1
    for num in numbers:
        yield sign * num
        sign *= -1   # flip sign each time

nums = [1, 2, 3, 4, 5]
for x in alternating_signs(nums):
    print(x, end=" ")   # 1 -2 3 -4 5
print()
