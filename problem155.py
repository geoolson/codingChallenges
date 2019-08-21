"""
This problem was asked by MongoDB.

Given a list of elements, find the majority element, which appears more than half the time (> floor(len(lst) / 2.0)).

You can assume that such element exists.

For example, given [1, 2, 1, 1, 3, 4, 0], return 1
"""
import math
import unittest
import collections

def majority(nums):
    bags = collections.Counter()
    for i in nums:
        bags[i] += 1
        if bags[i] >= math.floor(len(nums)/2.0):
            return i

class Test(unittest.TestCase):
    def setUp(self):
        self.input = [1,2,1,1,3,4,0]
    
    def test_majority(self):
        self.assertEqual(majority(self.input), 1)

if __name__ == "__main__":
    unittest.main()