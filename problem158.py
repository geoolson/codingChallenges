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