#!/usr/bin/python3
def count_vowels(string):
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for char in string.lower():
        if char in vowels:
            count += 1
    return count
