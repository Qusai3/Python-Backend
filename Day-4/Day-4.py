
# numbers= [5, 2, 3, 12, 7]
# large=numbers[0]
# second_num =numbers[0]
# for num in numbers:
#     if num>large:
#         second_num = large
#         large= num
#     elif num >second_num and num !=large:
#          second_num=num
# print("Second largest number is:", second_num)




# dic1 = {"a": 10, "b": 2}

# dic2 = {"c": 3, "d": 54}

# merged_dic = dic1 | dic2

# print("merge dics is:",merged_dic)













#create programm allow user enter students info

students = [] 

num_students = int(input("Enter number of students U WANT TO ADD IT TO THE LIST: "))

for i in range(num_students):
    print("Enter student info:", i+1)
    name = input("Enter name for student: ")
    age = input("Enter age: ")
    major = input("Enter major: ")

    student = (name, age, major)  
    students.append(student) 

print("Student List:")
for s in students:
    print("Name:", s[0], "-- Age:", s[1], "-- Major:", s[2])
