"""
This problem was asked by Triplebyte.

You are given n numbers as well as n probabilities that sum up to 1. Write a function to generate one of the numbers with its corresponding probability.

For example, given the numbers [1, 2, 3, 4] and probabilities [0.1, 0.5, 0.2, 0.2], your function should return 1 10% of the time, 2 50% of the time, and 3 and 4 20% of the time.

You can generate random numbers between 0 and 1 uniformly.
"""
import random
class Problem():
    def __init__(self, probs, nums):
        self.probs = probs
        self.nums = nums
        if(len(self.probs) != len(self.nums)):
            raise Exception("list of numbers and probabilities are not of equal length")
        self.ranges = self.checkProbSum()

    def checkProbSum(self):
        sum = 0
        ranges = []
        for i in self.probs:
            sum += i
            ranges.append(sum)
        if sum == 1 :
            return ranges
        else:
            raise Exception("sum of probabilities not equal to one")
        
    def randNum(self):
        randVal = random.random()
        for i in range(0, len(self.ranges)):
            if randVal < self.ranges[i]:
                return self.nums[i]

if __name__ == "__main__":
    problem = Problem([0.1,0.5,0.2,0.2], [1,2,3,4])
    for i in range(0,10):
        print(problem.randNum())