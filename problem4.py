"""
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""
import unittest

def positiveList(nums):
    posNums = []
    for i in nums:
        if i > 0:
            posNums.append(i)
    return posNums

def lowestInt(nums):
    nums = positiveList(nums)
    for i in range(0,len(nums)):
        if nums[i] <= len(nums):
            nums[abs(nums[i])-1] = -abs(nums[ abs(nums[i]) -1 ])
    for i in range(0,len(nums)):
        if nums[i] > 0:
            return i + 1
    return len(nums) + 1

class Test(unittest.TestCase):
    def setUp(self):
        self.input = [
            [3,4,-1,1],
            [1,2,0]
        ]
        self.expected = [2,3]
    
    def test_input1(self):
        self.assertEqual(lowestInt(self.input[0]), self.expected[0])
    def test_input2(self):
        self.assertEqual(lowestInt(self.input[1]), self.expected[1])

if __name__ == "__main__":
    unittest.main()