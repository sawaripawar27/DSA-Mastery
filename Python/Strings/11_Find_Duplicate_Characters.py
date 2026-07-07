"""
Author: Sawari
Language: Python
Topic: Strings

Problem:
Find duplicate characters in a string.

Description:
This program identifies and displays characters that appear
more than once in a string.

Algorithm:
1. Create an empty dictionary.
2. Traverse the string.
3. Count the frequency of each character.
4. Traverse the dictionary.
5. Print characters whose frequency is greater than 1.

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

print("Duplicate Characters:")

for key, value in frequency.items():
    if value > 1:
        print(key)
