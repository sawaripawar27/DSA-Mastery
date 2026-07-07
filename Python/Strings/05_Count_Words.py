"""
Author: Sawari
Language: Python
Topic: Strings

Problem:
Count the number of words in a string.

Description:
This program counts the total number of words present in a string.

Algorithm:
1. Initialize word count to 1.
2. Traverse the string.
3. Whenever a space is found, increment the word count.
4. Display the total number of words.

Time Complexity: O(n)
Space Complexity: O(1)
"""

string = "Python is easy to learn"

count = 1

for ch in string:
    if ch == " ":
        count += 1

print("Number of Words:", count)
