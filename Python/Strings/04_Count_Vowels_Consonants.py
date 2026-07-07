"""
Author: Sawari
Language: Python
Topic: Strings

Problem:
Count the number of vowels and consonants in a string.

Description:
This program counts vowels and consonants present in a string.

Algorithm:
1. Initialize vowel and consonant counters.
2. Traverse each character of the string.
3. Check if the character is an alphabet.
4. If it is a vowel, increment vowel count.
5. Otherwise, increment consonant count.
6. Display both counts.

Time Complexity: O(n)
Space Complexity: O(1)
"""

string = "Hello World"

vowels = 0
consonants = 0

for ch in string.lower():
    if ch.isalpha():
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
