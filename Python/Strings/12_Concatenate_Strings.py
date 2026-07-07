"""
Author: Sawari
Language: Python
Topic: Strings

Problem:
Concatenate two strings without using the '+' operator.

Description:
This program joins two strings by traversing each string
and appending their characters to a new string.

Algorithm:
1. Create two strings.
2. Initialize an empty string.
3. Traverse the first string and append each character.
4. Traverse the second string and append each character.
5. Display the concatenated string.

Time Complexity: O(n + m)
Space Complexity: O(n + m)
"""

string1 = "Hello"
string2 = "World"

result = ""

for ch in string1:
    result += ch

for ch in string2:
    result += ch

print("Concatenated String:", result)
