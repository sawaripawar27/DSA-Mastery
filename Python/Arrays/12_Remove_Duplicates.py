"""
Author: Sawari
Language: Python
Topic: Arrays

Problem:
Remove duplicate elements from an array.

Description:
This program removes duplicate elements while preserving
their original order by creating a new list.

Algorithm:
1. Create an empty list.
2. Traverse the original array.
3. Check if the current element is already present in the new list.
4. If not present, add it to the new list.
5. Display the array without duplicates.

Time Complexity: O(n²)
Space Complexity: O(n)
"""

arr = [10, 20, 30, 20, 40, 30, 50, 10]

unique = []

for i in arr:
    if i not in unique:
        unique.append(i)

print("Original Array:", arr)
print("Array after removing duplicates:", unique)
