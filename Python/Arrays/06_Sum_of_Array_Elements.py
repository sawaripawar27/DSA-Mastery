"""
Author: Sawari
Language: Python
Topic: Arrays

Problem:
Find the sum of all elements in an array.

Description:
This program calculates the sum of all elements in an array
by traversing each element and adding it to a variable.

Algorithm:
1. Initialize a variable 'sum' to 0.
2. Traverse the array.
3. Add each element to 'sum'.
4. Display the total sum.

Time Complexity: O(n)
Space Complexity: O(1)
"""

arr = [67, 89, 45, 91, 72]

sum = 0

for i in range(len(arr)):
    sum += arr[i]

print("Sum of Array Elements:", sum)
