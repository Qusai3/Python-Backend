
dic1 = { 'a': 1,
          'b': 2,
          'c': 3}

dic2 = {'b': 5,
         'd': 4}


merged = {}


for key, value in dic1.items():
    merged[key] = value


for key, value in dic2.items():
    if (old_value := merged.get(key)) is not None:
        merged[key] = value  
    else:
        merged[key] = value  


print("Merged dictionary:", merged)