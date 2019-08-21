"""
This problem was asked by Google.

Given an array of numbers and an index i, return the index of the nearest larger number of the number 
at index i, where distance is measured in array indices.

For example, given [4, 1, 3, 5, 6] and index 0, you should return 3.

If two distances to larger numbers are the equal, then return any one of them. If the array at i 
doesn't have a nearest larger integer, then return null.

Follow-up: If you can preprocess the array, can you do this in constant time?
"""
import unittest
import math

def nearestLarger(nums, index):
    num = nums[index]
    left = right = math.inf
    for i in range(index, len(nums)):
        if nums[i] > num:
            right = i
            break
    for i in range(index, 0, -1):
        if nums[i] > num:
            left = i
            break
    if abs(index - left) < abs(right - index):
        return left
    else:
        return right

class Test(unittest.TestCase):
    def setUp(self):
        self.input = [
            [4,1,3,5,6],
            [1,4,3,2,5]
        ]
        self.expected = [3,1]
    
    def test_problem(self):
        self.assertEqual(nearestLarger(self.input[0], 0), self.expected[0])
    
    def test_problem2(self):
        self.assertEqual(nearestLarger(self.input[1], 2), self.expected[1])

if __name__ == "__main__":
    unittest.main()