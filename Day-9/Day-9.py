import time

def measure_time(func):
    def wrapper(*args, **kwargs):  
        start = time.time()
        result = func(*args, **kwargs)  
        end = time.time()
        execution_time = end - start
        print(f"Execution time: {execution_time:.4f} seconds")
        return result
    return wrapper

@measure_time
def slow_function():
    total = 0
    for i in range(1, 1000000):
        total += i
    return total

def write_result_to_file(filename, content):
    with open(filename, "w") as f:
        f.write(content)

result = slow_function()
print("Result:", result)

write_result_to_file("output(Day-9.py).txt", f"Final result: {result}\n")
print("Result written to output.txt")