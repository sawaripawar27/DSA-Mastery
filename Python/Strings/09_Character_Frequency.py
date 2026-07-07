"""
Author: Sawari
Language: Python
Topic: Strings

Problem:
Find the frequency of each character in a string.

Description:
This program counts the number of occurrences of each
character in a string.

Algorithm:
1. Create an empty dictionary.
2. Traverse the string.
3. If the character already exists, increment its count.
4. Otherwise, add it with count 1.
5. Display each character with its frequency.

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

for key, value in frequency.items():
    print(key, ":", value)
