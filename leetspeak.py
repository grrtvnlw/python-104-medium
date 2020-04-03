# given text as a string, print the text in leetspeak
# get user input as a string // lowercase the input
inp = input("Give me some text! ").lower()
# creat a new variable to return to the user / list for now, will convert to string
new_string = []
# check each letter in the string
for letter in inp:
    if letter == "a":
        letter = letter.replace("a", "4")
        new_string.append(letter)
    elif letter == "e":
        letter = letter.replace("e", "3")
        new_string.append(letter)
    elif letter == "g":
        letter = letter.replace("g", "6")
        new_string.append(letter)
    elif letter == "i":
        letter = letter.replace("i", "1")
        new_string.append(letter)
    elif letter == "o":
        letter = letter.replace("o", "0")
        new_string.append(letter)
    elif letter == "s":
        letter = letter.replace("s", "5")
        new_string.append(letter)
    elif letter == "t":
        letter = letter.replace("t", "7")
        new_string.append(letter)
    else:
        new_string.append(letter)
# convert the list to a string
new_string = ''.join(new_string)
# print the new string
print(new_string)