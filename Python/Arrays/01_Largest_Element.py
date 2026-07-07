"""
Author: Sawari
Language: Python
Topic: Arrays

Problem:
Find the largest element in an array.

Description:
This program traverses the array and identifies the largest element by
comparing each element with the current maximum value.

Algorithm:
1. Store the first array element as the largest.
2. Traverse the array from the second element.
3. Compare each element with the current largest value.
4. If a larger element is found, update the largest value.
5. Display the largest element.

Time Complexity: O(n)
Space Complexity: O(1)
"""

arr = [67, 89, 45, 91, 72]

largest = arr[0]

for i in range(1, len(arr)):
    if arr[i] > largest:
        largest = arr[i]

print("Largest Element:", largest)
