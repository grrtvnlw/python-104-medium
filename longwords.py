# given a word as a string, extend any long vowels to the length of five
# get user input and set up compare variable
inp = input("Give me a string! ")
compare = ''
# create a new variable to return to the new string, will convert list to string
new_string = []
# check each letter in the input
for index in range(len(inp)):
    # letter equals the value at each index of the input
    letter = inp[index]
    # test and see if previous letter = current letter
    if compare == letter:
        # if previous letter equals current letter, multiply letter by 4
        letter = letter * 4
        new_string.append(letter)
    # if the letters don't match, add only one letter
    else:
        new_string.append(letter)
    # set compare variable to current letter and end of loop
    compare = inp[index]
# convert the list to a string
new_string = ''.join(new_string)
# print the new string
print(new_string)