# given a name from a user, remove the last vowel from the name
inp = input("What's the name of your startup? ")
# create vowels variable and current char, next char holders
vowels = 'aeiouy'
next_char = ''
current_char = ''
# creat a variable for the new string that is a list
new_string = []
# create counter variable and set equal to one less than len(input) so we can start at the last index
counter = (len(inp) - 1)
# create variable for "on-off" switch to skip only one vowel
skip = 0
# start counting from the end of the string
while 0 <= counter:
    # set variable for current letter in string
    current_char = inp[counter]
    # set variable for the next letter in string 
    next_char = inp[counter - 1]
    # if current letter is not a vowel, add it to the front of the new string
    if current_char not in vowels:
       new_string.insert(0, current_char) 
    # if current character is a vowel, check the conditions
    elif current_char in vowels:
        # if it is a vowel and the last letter of the string, add it to the new string
        if current_char == inp[-1]:
            new_string.insert(0, current_char)
        # if it is a vowel and not the last letter
        elif current_char in vowels:
            # do not add the vowel / close the on-off switch
            if skip == 0:
                skip = 1
            # the next vowel will be added to the new string since the skip switch is now off
            elif skip != 0:
                new_string.insert(0, current_char)
    # decrement counter to move to next letter
    counter -= 1
# convert the new string list to a string
new_string = ''.join(new_string)
print(new_string)
