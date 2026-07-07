"""
Author: Sawari
Language: Python
Topic: Strings

Problem:
Find the first non-repeating character in a string.

Description:
This program finds the first character that appears only once
in a string.

Algorithm:
1. Create an empty dictionary.
2. Count the frequency of each character.
3. Traverse the string again.
4. Print the first character whose frequency is 1.
5. Stop the search.

Time Complexity: O(n)
Space Complexity: O(n)
"""

string = "programming"

frequency = {}

for ch in string:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

for ch in string:
    if frequency[ch] == 1:
        print("First Non-Repeating Character:", ch)
        break
