"""
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers 
from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true 
since 10 + 7 is 17.

Bonus: Can you do this in one pass
"""
import unittest

def canSum(inputNums, k):
    for i in range(0,len(inputNums)):
        for j in range(i+1, len(inputNums)):
            if (inputNums[j] + inputNums[i] == k):
                return True
    return False

def onePass(inputNums, k):
    checkedVals = set()
    for i in inputNums:
        checkedVals.add(i)
        if (k-i in checkedVals):
            return True
    return False

class Problem(unittest.TestCase):
    def setUp(self):
        self.inputNums = [10, 5, 3, 7]
        self.k = 17
    def test_true(self):
        self.assertTrue(canSum(self.inputNums, self.k))

    def test_onePass(self):
        self.assertTrue(onePass(self.inputNums, self.k))

if __name__ == '__main__':
    unittest.main()