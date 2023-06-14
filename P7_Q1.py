from collections import Counter

def count_chars(s):
    temp = {}
    char_counts = Counter(s)
    for char, count in char_counts.items():
        temp[char]  = int(count) 
    return temp 

s = input("Enter the sequence:\n")

temp = count_chars(s)

for key in temp:
    temp[key] = temp[key]*100/len(s)
    print(f"% Composition of {key}: {temp[key]:.2f}") 

