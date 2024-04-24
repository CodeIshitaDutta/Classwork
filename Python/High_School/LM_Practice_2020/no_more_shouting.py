string_analyzed = input("enter a string: ")

for i in range(len(string_analyzed)):
    if string_analyzed[i].isupper():
        new_letter = string_analyzed[i].lower()
        string_analyzed = string_analyzed[:i] + new_letter + string_analyzed[i+1:]

print(string_analyzed)
