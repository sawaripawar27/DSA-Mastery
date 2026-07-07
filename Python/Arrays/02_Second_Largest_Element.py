"""
Author: Sawari
Language: Python
Topic: Arrays

Problem:
Find the second largest element in an array.

Description:
This program finds both the largest and the second largest elements
by traversing the array only once.

Algorithm:
1. Initialize 'largest' and 'second_largest' with the first element.
2. Traverse the array from the second element.
3. If the current element is greater than 'largest':
   - Update 'second_largest' with the current 'largest'.
   - Update 'largest' with the current element.
4. Else if the current element is greater than 'second_largest'
   and not equal to 'largest':
   - Update 'second_largest'.
5. Display both the largest and second largest elements.

Time Complexity: O(n)
Space Complexity: O(1)
"""

arr = [67, 89, 45, 91, 72, 105]

largest = arr[0]
second_largest = arr[0]

for i in range(1, len(arr)):
    if arr[i] > largest:
        second_largest = largest
        largest = arr[i]
    elif arr[i] > second_largest and arr[i] != largest:
        second_largest = arr[i]

print("Largest Element:", largest)
print("Second Largest Element:", second_largest)
