"""
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""
import unittest

def products(nums):
    result = []
    product = nums[0]
    for i in range(1, len(nums)):
        product *= nums[i]
    for i in nums:
        result.append(product/i)
    return result


class Test(unittest.TestCase):
    def setUp(self):
        self.nums = [1,2,3,4,5]
        self.result = [120,60,40,30,24]

    def test_products(self):
        self.assertListEqual( products(self.nums), self.result )

if __name__ == "__main__":
    unittest.main()