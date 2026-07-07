"""
Author: Sawari
Language: Python
Topic: Strings

Problem:
Reverse a string.

Description:
This program reverses a string by traversing it from the last
character to the first.

Algorithm:
1. Initialize an empty string.
2. Traverse the original string from the last index to the first.
3. Append each character to the new string.
4. Display the reversed string.

Time Complexity: O(n)
Space Complexity: O(n)
"""

string = "Python"

reverse = ""

for i in range(len(string) - 1, -1, -1):
    reverse += string[i]

print("Reversed String:", reverse)
