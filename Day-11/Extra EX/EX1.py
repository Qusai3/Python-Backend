import re

def validateemail(email):
    pattern = r'^[A-Za-z0-9.-]+@[A-Za-z0-9-]+.[A-Za-z]{2,4}$'
    return re.match(pattern, email) is not None



print(validateemail("john.doe@example.com"))  
print(validateemail("bad@domain"))           
print(validateemail("name.org"))        