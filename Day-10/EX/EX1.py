class FibonacciIterator:
    def __init__(self, n):
        self.n = n          
        self.count = 0      
        self.a, self.b = 0, 1  

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration  
        self.count += 1
        value = self.a
        self.a, self.b = self.b, self.a + self.b  
        return value


fib = FibonacciIterator(10)
for num in fib:
    print(num, end=" ")  