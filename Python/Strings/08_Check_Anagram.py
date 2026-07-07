"""
Author: Sawari
Language: Python
Topic: Strings

Problem:
Check whether two strings are anagrams.

Description:
This program checks whether two strings are anagrams by
sorting their characters and comparing the results.

Algorithm:
1. Input two strings.
2. Convert both strings to lowercase.
3. Sort both strings.
4. Compare the sorted strings.
5. Display the result.

Time Complexity: O(n log n)
Space Complexity: O(n)
"""

string1 = "listen"
string2 = "silent"

if sorted(string1.lower()) == sorted(string2.lower()):
    print("Strings are Anagrams")
else:
    print("Strings are Not Anagrams")
