"""
Author: Sawari
Language: Python
Topic: Arrays

Problem:
Check whether an array is sorted in ascending order.

Description:
This program checks if every element is smaller than or equal to
its next element. If any element is greater than the next one,
the array is not sorted.

Algorithm:
1. Assume the array is sorted.
2. Traverse the array from the first element to the second last.
3. Compare each element with the next element.
4. If the current element is greater than the next element,
   mark the array as not sorted.
5. Display the result.

Time Complexity: O(n)
Space Complexity: O(1)
"""

arr = [10, 20, 30, 40, 50]

sorted = True

for i in range(len(arr) - 1):
    if arr[i] > arr[i + 1]:
        sorted = False
        break

if sorted:
    print("Array is sorted.")
else:
    print("Array is not sorted.")
