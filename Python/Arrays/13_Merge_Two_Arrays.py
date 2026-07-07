"""
Author: Sawari
Language: Python
Topic: Arrays

Problem:
Merge two arrays into a single array.

Description:
This program combines two arrays into one by
adding all elements of the second array to the first.

Algorithm:
1. Create two arrays.
2. Create an empty array for storing merged elements.
3. Traverse the first array and add each element to the merged array.
4. Traverse the second array and add each element to the merged array.
5. Display the merged array.

Time Complexity: O(n + m)
Space Complexity: O(n + m)
"""

arr1 = [10, 20, 30]
arr2 = [40, 50, 60]

merged = []

for i in arr1:
    merged.append(i)

for i in arr2:
    merged.append(i)

print("Merged Array:", merged)
