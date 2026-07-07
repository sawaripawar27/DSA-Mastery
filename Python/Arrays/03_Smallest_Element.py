"""
Author: Sawari
Language: Python
Topic: Arrays

Problem:
Find the smallest element in an array.

Description:
This program traverses the array and identifies the smallest element
by comparing each element with the current minimum value.

Algorithm:
1. Assume the first element is the smallest.
2. Traverse the array from the second element.
3. Compare each element with the current smallest value.
4. If a smaller element is found, update the smallest value.
5. Display the smallest element.

Time Complexity: O(n)
Space Complexity: O(1)
"""

arr = [67, 89, 45, 91, 72]

smallest = arr[0]

for i in range(1, len(arr)):
    if arr[i] < smallest:
        smallest = arr[i]

print("Smallest Element:", smallest)
