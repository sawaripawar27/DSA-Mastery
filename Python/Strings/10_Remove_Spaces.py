"""
Author: Sawari
Language: Python
Topic: Strings

Problem:
Remove all spaces from a string.

Description:
This program removes all spaces from a string by traversing
each character and storing only non-space characters.

Algorithm:
1. Initialize an empty string.
2. Traverse each character of the string.
3. If the character is not a space, append it.
4. Display the updated string.

Time Complexity: O(n)
Space Complexity: O(n)
"""

string = "Python is easy to learn"

result = ""

for ch in string:
    if ch != " ":
        result += ch

print("String without spaces:", result)
