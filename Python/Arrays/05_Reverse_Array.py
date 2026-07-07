"""
Author: Sawari
Language: Python
Topic: Arrays

Problem:
Reverse the elements of an array.

Description:
This program reverses an array using the two-pointer approach.
The first and last elements are swapped, then the pointers move
towards the center until the entire array is reversed.

Algorithm:
1. Initialize two pointers:
   - left = 0
   - right = last index
2. Swap the elements at left and right.
3. Increment left and decrement right.
4. Repeat until left is less than right.
5. Display the reversed array.

Time Complexity: O(n)
Space Complexity: O(1)
"""

arr = [67, 89, 45, 91, 72]

left = 0
right = len(arr) - 1

while left < right:
    temp = arr[left]
    arr[left] = arr[right]
    arr[right] = temp

    left += 1
    right -= 1

print("Reversed Array:", arr)
