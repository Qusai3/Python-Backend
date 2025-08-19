text = "Programming is awesome!"

vowels_set = {ch.upper() for ch in text if ch.lower() in "aeiou"}
print(vowels_set)   # {'A', 'O', 'E', 'I'}