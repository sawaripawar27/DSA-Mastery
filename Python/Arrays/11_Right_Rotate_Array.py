"""
Author: Sawari
Language: Python
Topic: Arrays

Problem:
Right Rotate an Array by One Position.

Description:
This program shifts every element one position to the right.
The last element is moved to the first position.

Algorithm:
1. Store the last element in a temporary variable.
2. Shift all elements one position to the right.
3. Place the last element at the first index.
4. Display the rotated array.

Time Complexity: O(n)
Space Complexity: O(1)
"""

arr = [10, 20, 30, 40, 50]

last = arr[len(arr) - 1]

for i in range(len(arr) - 1, 0, -1):
    arr[i] = arr[i - 1]

arr[0] = last

print("Right Rotated Array:", arr)
