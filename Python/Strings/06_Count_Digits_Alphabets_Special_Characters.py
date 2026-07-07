"""
Author: Sawari
Language: Python
Topic: Strings

Problem:
Count digits, alphabets, and special characters in a string.

Description:
This program counts the number of digits, alphabets,
and special characters present in a string.

Algorithm:
1. Initialize counters for digits, alphabets, and special characters.
2. Traverse each character of the string.
3. Check the type of each character.
4. Increment the corresponding counter.
5. Display all counts.

Time Complexity: O(n)
Space Complexity: O(1)
"""

string = "Python123@# AI"

digits = 0
alphabets = 0
special = 0

for ch in string:
    if ch.isdigit():
        digits += 1
    elif ch.isalpha():
        alphabets += 1
    elif ch != " ":
        special += 1

print("Digits:", digits)
print("Alphabets:", alphabets)
print("Special Characters:", special)
