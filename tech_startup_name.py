# given a name from a user, remove the last vowel that comes before a non-vowel
inp = input("What's the name of your startup? ")
# create vowels variable
vowels = 'aeiouyAEIOUY'
# create a variable for the new string that will be an empty list for now
new_string = []
# create counter variable and set equal to one less than len(input) so we can start at the last index
counter = (len(inp) - 1)
# create variable for "on-off" switch to skip only one vowel
skip = 0
# start counting from the end of the string
while 0 <= counter:
    # set variable for current letter in string to be equal to the current index of the string
    current_char = inp[counter]
    # if current letter is not a vowel, add it to the front of the new_string list
    if current_char not in vowels:
        new_string.insert(0, current_char) 
    # if current letter is a vowel, check the following conditions
    else:
        # if it is a vowel and the last letter of the string, add it to the new string
        if counter == (len(inp) - 1):
            new_string.insert(0, current_char)
        # if it is a vowel and not the last letter
        else:
            # do not add the first vowel that is not the last letter of the string
            # skip this vowel and close the on-off switch
            if skip == 0:
                skip = 1
            # the next vowel will be added to the new string since the skip switch is now closed
            else:
                new_string.insert(0, current_char)
    # decrement counter to move to next letter
    counter -= 1
# convert the new string list to a string
new_string = ''.join(new_string)
print(new_string)