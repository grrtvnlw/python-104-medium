# given text as a string, print the text in leetspeak
# get user input as a string // lowercase the input
inp = input("Give me some text! ").lower()
# create a variable for new string, set equal to empty string
new_string = ''
# check each letter in the string
for letter in inp:
    # if letter matches a certain letter, change that letter and add to new string
    if letter == "a":
        letter = "4"
        new_string += letter
    elif letter == "e":
        letter = "3"
        new_string += letter
    elif letter == "g":
        letter = "6"
        new_string += letter
    elif letter == "i":
        letter = "1"
        new_string += letter
    elif letter == "o":
        letter = "0"
        new_string += letter
    elif letter == "s":
        letter = "5"
        new_string += letter
    elif letter == "t":
        letter = "7"
        new_string += letter
    # if letter does not match a certain letter, add the original letter to new string
    else:
        new_string += letter
# print the new string
print(new_string)