#!/usr/bin/python3
for letter in range(26):
    if letter == 'e' or letter == 'q':
        letter += 1
    print("{}".format(chr(97 + letter)), end="")
