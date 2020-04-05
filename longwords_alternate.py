# given a word as a string, extend any long vowels to the length of five
# get user input and set up compare variable and vowels variable
inp = input("Give me a string! ")
prev_char = ''
vowels = 'aeiouy'
# create a variable for the new string
new_string = ''
# check each letter in the input
for letter in inp:
    # set up current letter variable
    current_char = letter
    # test and see if previous letter = current letter
    if prev_char == current_char:
        # test if double letters are vowels
        if current_char in vowels:
            # if previous letter equals current letter and is a vowel, multiply letter by 4
            current_char *= 4
            new_string += current_char
        else: 
            new_string += current_char
    # if the letters don't match, add only the current letter
    else:
        new_string += current_char
    # set previous letter to current letter at end of loop
    prev_char = letter
# print the new string
print(new_string)