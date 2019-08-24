"""
This problem was asked by Slack.

You are given an N by M matrix of 0s and 1s. Starting from the top left corner, how many ways are there to reach the bottom right corner?

You can only move right and down. 0 represents an empty space while 1 represents a wall you cannot walk through.

For example, given the following matrix:

[[0, 0, 1],
 [0, 0, 1],
 [1, 0, 0]]
Return two, as there are only two ways to get to the bottom right:

Right, down, down, right
Down, right, down, right
The top left corner and bottom right corner will always be 0
"""
import unittest
import queue

def paths(maze):
    dimY, dimX = len(maze), len(maze[0])
    paths = queue.Queue()
    current = (0,0)
    paths.put(current)
    sumPaths = 0
    while not paths.empty():
        current = paths.get()
        if current[0] < dimY and current[1] < dimX:
            if current[0] == dimY-1 and current[1] == dimX-1:
                sumPaths+= 1
            if maze[current[0]][current[1]] == 0:
                paths.put((current[0]+1, current[1]))
                paths.put((current[0], current[1]+1))
    return sumPaths

class Test(unittest.TestCase):
    def setUp(self):
        self.input = [
            [0,0,1],
            [0,0,1],
            [1,0,0]
        ]
        self.expected = 2
    
    def test_maze(self):
        self.assertEqual(paths(self.input), 2)

if __name__ == "__main__":
    unittest.main()