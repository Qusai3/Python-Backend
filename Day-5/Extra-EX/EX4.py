dic1 = {"a": 1, "b": 2}
dic2 = {"b": 3, "c": 4}

merged = {}

for key, value in dic1.items():
    merged[key] = value

for key, value in dic2.items():
    if (old_value := merged.get(key)) is not None:
        
        merged[key + "_resolved"] = old_value + value
        del merged[key]
    else:
        merged[key] = value

print("Merged dictionary:", merged)
