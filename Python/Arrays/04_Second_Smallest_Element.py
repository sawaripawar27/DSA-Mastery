"""
Author: Sawari
Language: Python
Topic: Arrays

Problem:
Find the second smallest element in an array.

Description:
This program finds the smallest and second smallest elements
by traversing the array only once.

Algorithm:
1. Initialize 'smallest' and 'second_smallest' with the first element.
2. Traverse the array from the second element.
3. If the current element is smaller than 'smallest':
   - Store the current smallest as second smallest.
   - Update the smallest.
4. Otherwise, if the current element is smaller than the second smallest
   and not equal to the smallest, update the second smallest.
5. Display the smallest and second smallest elements.

Time Complexity: O(n)
Space Complexity: O(1)
"""

arr = [67, 89, 45, 91, 72, 30]

smallest = arr[0]
second_smallest = arr[0]

for i in range(1, len(arr)):
    if arr[i] < smallest:
        second_smallest = smallest
        smallest = arr[i]
    elif arr[i] < second_smallest and arr[i] != smallest:
        second_smallest = arr[i]

print("Smallest Element:", smallest)
print("Second Smallest Element:", second_smallest)
