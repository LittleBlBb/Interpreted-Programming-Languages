input_string = input()
input_string = input_string.split()
dictionary = {}
for word in input_string:
    if word in dictionary:
        dictionary[word] += 1
    else:
        dictionary[word] = 0
print(dictionary.items())