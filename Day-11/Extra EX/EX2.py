import re 

def extract_dates(text):
    pattern = r'\b\d{2}[-/]\d{2}[-/]\d{4}\b'
    return re.findall(pattern, text)

sample = "10-05-2002, 01/01/2022, and 25-10-2025."
print(extract_dates(sample))