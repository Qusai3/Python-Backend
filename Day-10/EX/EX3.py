words = ["hello", "cat"]

ascii_dict = {
    word: {ch: ord(ch) for ch in word}
    for word in words
}

print(ascii_dict)

{
'hello': {'h': 104, 'e': 101, 'l': 108, 'o': 111},
'cat': {'c': 99, 'a': 97, 't': 116}
}