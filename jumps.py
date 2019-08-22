"""
Given an array of non-negative integers, you are initially 
positioned at the first index of the array.

Each element in the array represents your maximum jump 
length at that position.

Determine if you are able to reach the last index.
"""
import unittest
import sys
class Problem:
    def __init__(self):
        self.success = False
        self.checked = set()

    def _hops(self, nums, index):
        if self.success or index in self.checked:
            return
        self.checked.add(index)
        jumps = nums[index]
        if index+jumps >= len(nums)-1:
            self.success = True
            return
        elif jumps == 0:
            return
        else:
            for i in range(index, index+jumps):
                if self.success:
                    return
                self._hops(nums, i+1)

    def hops(self, nums):
        for i in range(0, len(nums)-1):
            if nums[i] == 0:
                self.checked.add(i)
        self.success = False
        self._hops(nums, 0)
        return self.success

def hopsGreedy(nums):
    current = next = 0
    jump = furthestJump = nums[current]
    while next + nums[next] < len(nums)-1:
        current = next
        jump = nums[current]
        endLoop = jump+current+1
        for i in range(current, endLoop):
            if nums[i] + i>= furthestJump:
                furthestJump = i + nums[i] 
                next = i
        if current == next:
            return False
    return True


class Test(unittest.TestCase):
    def setUp(self):
        self.hops = hopsGreedy
        self.input = [
            [2,3,1,1,4],
            [3,2,1,0,4],
            [8,2,4,4,4,9,5,2,5,8,8,0,8,6,9,1,1,6,3,5,1,2,6,6,0,4,8,6,0,3,2,8,7,6,5,1,7,0,3,4,8,3,5,9,0,4,0,1,0,5,9,2,0,7,0,2,1,0,8,2,5,1,2,3,9,7,4,7,0,0,1,8,5,6,7,5,1,9,9,3,5,0,7,5],
            list(range(500, 0, -1)) + [1,0,0,0],
            [2,0,1,0],
            [1,1,0,1]
        ]
    def test_one(self):
        self.assertTrue(self.hops(self.input[0]))
    def test_two(self):
        self.assertFalse(self.hops(self.input[1]))
    def test_three(self):
        self.assertTrue(self.hops(self.input[2]))
    def test_four(self):
        self.assertFalse(self.hops(self.input[3]))
    def test_five(self):
        self.assertTrue(self.hops(self.input[4]))
    def test_six(self):
        self.assertFalse(self.hops(self.input[5]))

if __name__ == "__main__":
    unittest.main()