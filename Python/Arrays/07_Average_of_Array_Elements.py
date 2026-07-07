"""
Author: Sawari
Language: Python
Topic: Arrays

Problem:
Find the average of all elements in an array.

Description:
This program calculates the average of all elements in an array
by finding the total sum and dividing it by the number of elements.

Algorithm:
1. Initialize a variable 'sum' to 0.
2. Traverse the array and add each element to 'sum'.
3. Divide the sum by the total number of elements.
4. Display the average.

Time Complexity: O(n)
Space Complexity: O(1)
"""

arr = [67, 89, 45, 91, 72]

sum = 0

for i in range(len(arr)):
    sum += arr[i]

average = sum / len(arr)

print("Average of Array Elements:", average)
