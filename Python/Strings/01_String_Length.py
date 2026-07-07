"""
Author: Sawari
Language: Python
Topic: Strings

Problem:
Find the length of a string without using the len() function.

Description:
This program calculates the length of a string by traversing each character.

Algorithm:
1. Initialize count to 0.
2. Traverse each character.
3. Increment count.
4. Display the length.

Time Complexity: O(n)
Space Complexity: O(1)
"""

string = "Python"

count = 0

for ch in string:
    count += 1

print("Length of String:", count)
