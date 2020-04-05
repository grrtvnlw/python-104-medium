# given a word as a string, extend any long vowels to the length of five
# get user input and set up compare variable and vowels variable
inp = input("Give me a string! ")
prev_char = ''
vowels = 'aeiouy'
# create a new variable to return to the new string, will convert list to string
new_string = []
# check each letter in the input
for index in range(len(inp)):
    # current letter equals the current index value
    current_char = inp[index]
    # test and see if previous letter = current letter
    if prev_char == current_char:
        # test if double letters are vowels
        if current_char in vowels:
            # if previous letter equals current letter and is a vowel, multiply letter by 4
            current_char *= 4
            new_string.append(current_char)
        else: 
            new_string.append(current_char)
    # if the letters don't match, add only one letter
    else:
        new_string.append(current_char)
    # set previous letter to current letter at end of loop
    prev_char = inp[index]
# convert the list to a string
new_string = ''.join(new_string)
# print the new string
print(new_string)