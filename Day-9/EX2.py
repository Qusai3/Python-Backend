def call_counter(func):
    def x(args, **kwargs):
        x.count += 1
        return func(args, **kwargs)
    x.count = 0   
    return x

@call_counter
def names(name):
    return "Hello, " + name 


print(names("Qusai"))
print(names("Omar"))
print(names("Sameer"))
print("number of names was called:", names.count, "times")    
