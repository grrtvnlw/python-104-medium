# given a word as a string, extend any long vowels to the length of five
# get user input and set up compare variable and vowels variable
inp = input("Give me a string! ")
compare = ''
vowels = 'aeiouy'
# create a variable for the new string and set it equal to an empty string
new_string = ''
# check each letter in the input
for index in range(len(inp)):
    # letter equals the value at each index of the input
    letter = inp[index]
    # test and see if previous letter = current letter
    if compare == letter:
        # test if double letters are vowels
        if letter in vowels:
            # if previous letter equals current letter and is a vowel, multiply letter by 4
            letter = letter * 4
            new_string += letter
    # if the letters don't match, add only one letter
    else:
        new_string += letter
    # set compare variable to current letter and end of loop
    compare = inp[index]
# print the new string
print(new_string)