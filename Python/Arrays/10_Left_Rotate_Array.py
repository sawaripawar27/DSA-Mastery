"""
Author: Sawari
Language: Python
Topic: Arrays

Problem:
Left Rotate an Array by One Position.

Description:
This program shifts every element one position to the left.
The first element is moved to the last position.

Algorithm:
1. Store the first element in a temporary variable.
2. Shift all elements one position to the left.
3. Place the first element at the last index.
4. Display the rotated array.

Time Complexity: O(n)
Space Complexity: O(1)
"""

arr = [10, 20, 30, 40, 50]

first = arr[0]

for i in range(len(arr) - 1):
    arr[i] = arr[i + 1]

arr[len(arr) - 1] = first

print("Left Rotated Array:", arr)
