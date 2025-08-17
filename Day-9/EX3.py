def validate_positive_numbers(func):
    def wrapper(*args, **kwargs):  
        
        for a in args:
            if not (isinstance(a, (int, float)) and a > 0):
                raise ValueError("All arguments must be positive numbers (> 0).")
    
        for a in kwargs.values():
            if not (isinstance(a, (int, float)) and a > 0):
                raise ValueError("All arguments must be positive numbers (> 0).")
        return func(*args, **kwargs)  
    return wrapper

@validate_positive_numbers
def add(a, b):
    return a + b

@validate_positive_numbers
def rectangle_area(length, width):
    return length * width  

print("Add two numbers: ", add(3, 5))
print("Rectangle area (4, 6):", rectangle_area(4, 6))