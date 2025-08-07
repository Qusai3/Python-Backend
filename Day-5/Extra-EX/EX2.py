# student ={
#     "name":"qusai",
#     "age": 20,
#     "skills": ["Python", "JavaScript", "C++"]
# }
# print("Student INFO: ",student)


# numbers =[3,4,8,7,9,9,3]
# unique_numbers = list(set(numbers))
# print("Unique numbers:", unique_numbers)




text = "hello Qusai hello"

words = text.split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word frequencies:", word_count)





squares = {x: x * x for x in range(1, 6)}

print("Squares:", squares)
