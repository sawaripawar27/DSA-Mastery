"""
Author: Sawari
Language: Python
Topic: Arrays

Problem:
Perform Linear Search on an array.

Description:
This program searches for a given element in an array using
the Linear Search algorithm. If the element is found, its
index is displayed; otherwise, an appropriate message is shown.

Algorithm:
1. Store the element to be searched.
2. Traverse the array from the first element.
3. Compare each element with the search element.
4. If a match is found, display its index and stop searching.
5. If no match is found after traversing the array, display
   "Element not found".

Time Complexity: O(n)
Space Complexity: O(1)
"""

arr = [67, 89, 45, 91, 72]

key = 91
found = False

for i in range(len(arr)):
    if arr[i] == key:
        print("Element found at index:", i)
        found = True
        break

if not found:
    print("Element not found")
