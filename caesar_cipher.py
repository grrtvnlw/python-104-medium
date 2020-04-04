# given a string, print the Caeser Cipher of that string
# get user input as a string and lowercase the input
inp = input("Give me a string, please: ").lower()
# set up an empty list for the new string
new_string = []
# convert each letter in the string to ordinal value
for letter in inp:
    letter = ord(letter)
    # add 13 to each ordinal value
    letter += 13
    # if letter ordinal value goes over 122 "z" value
    if letter > 122:
    # find the remainder and add that to 96 "a" value
        letter = letter % 122 + 96
    # convert ordinal value back to character value
    letter = chr(letter)
    # add character value to the new string
    new_string.append(letter)
# convert list to string
new_string = ''.join(new_string)
print(new_string)