#!/bin/python3
"""
Is Unique: Implement an algorithm to determine if a string has all unique
characters.

What if you cannot use additional data structures?
"""

def is_unique(sentence):

    # Assumes is ascii 128
    ascii = [False] * 128

    if len(sentence) > 128:
        return False

    for char in sentence:
        if ascii[ord(char)] == False:
            ascii[ord(char)] = True
        else:
            # Is not unique
            return False
    return True

if __name__ == "__main__":
    s = input()
    print(is_unique(s))
