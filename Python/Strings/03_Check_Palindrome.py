"""
Author: Sawari
Language: Python
Topic: Strings

Problem:
Check whether a string is a palindrome.

Description:
This program checks whether a string reads the same
from left to right and right to left.

Algorithm:
1. Store the original string.
2. Reverse the string.
3. Compare the original string with the reversed string.
4. If both are equal, the string is a palindrome.
5. Otherwise, it is not a palindrome.

Time Complexity: O(n)
Space Complexity: O(n)
"""

string = "madam"

reverse = ""

for i in range(len(string) - 1, -1, -1):
    reverse += string[i]

if string == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")
