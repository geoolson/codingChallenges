"""

This problem was asked by Amazon.

Given a string, determine whether any permutation of it is a palindrome.

For example, carrace should return true, since it can be rearranged to form 
racecar, which is a palindrome. daily should return false, since there's no 
rearrangement that can form a palindrome.
"""
import unittest
import collections

def canPalindrome(inStr):
    counter = collections.Counter(inStr)
    sumOdds = 0
    for i in range(0, len(counter)):
        if counter[i]%2 == 1:
            sumOdds += 1
            if sumOdds > 1:
                return False
    return True


class Test(unittest.TestCase):
    def setUp(self):
        self.input = [
            "carrace"
            "daily"
            "aab"
        ]
        self.expected = [True, False, True]

    def tearDown(self):
        pass
    
    def test_canPalindrome(self):
        for i, j in zip(self.input, self.expected):
            self.assertEqual(canPalindrome(i), j)

if __name__ == "__main__":
    unittest.main()