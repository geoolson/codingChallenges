"""
Good morning! Here's your coding interview problem for today.

Given a list, sort it using this method: reverse(lst, i, j), which reverses lst 
from i to j
"""
import unittest
import random
import copy

def reverselst(lst, i, j):
    reversed = list(lst[i:j])
    reversed.reverse()
    return lst[:i] + reversed + lst[j:]

def panSort(lst):
    for i in range(0, len(lst)):
        largest = 0
        index = 0
        for j in range(i, len(lst)):
            if lst[j] >= largest:
                largest = lst[j]
                index = j
        lst = reverselst(lst, i, index+1)
    lst.reverse()
    return lst

class Test(unittest.TestCase):
    def test_sort(self):
        random.seed(30)
        mixedlst = [ random.random() for i in range(0,500)]
        lstcopy = copy.deepcopy(mixedlst)
        lstcopy.sort()
        self.assertListEqual(panSort(mixedlst), lstcopy)

if __name__ == "__main__":
    unittest.main()
