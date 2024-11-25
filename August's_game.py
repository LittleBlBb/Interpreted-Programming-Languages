def delete_item(b_array, a_array):
    for item in b_array:
        if item in a_array:
            a_array.remove(item)
    return a_array

def set_array(b_array, a_array):
    a_array.clear()
    for item in b_array:
        a_array.append(item)
    return a_array

def august_answer(b_array, a_array):
    c = 0
    for item in b_array:
        if item in a_array:
            c += 1
    if c <= len(a_array) / 2:
        delete_item(b_array, a_array)
        return False
    else:
        b_array_copy = b_array[:]
        for item in b_array_copy:
            if item not in a_array:
                b_array.remove(item)
        set_array(b_array, a_array)
        return True

print("Input August's number:")
guess = int(input())
August_array = []
for i in range(1, guess + 1):
    August_array.append(i)
print("Input Beatrice's question on same line")
question = input()
while question != "HELP":
    Beatrice_array = [int(item) for item in question.split() if item.isdigit()]
    if august_answer(Beatrice_array, August_array):
        print("YES")
    else:
        print("NO")
    print("Input Beatrice's question on same line")
    question = input()

print(August_array)