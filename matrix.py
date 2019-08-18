"""
Good morning! Here's your coding interview problem for today.

Given a 2-D matrix representing an image, a location of a pixel in the screen and a color C, replace the color of the given pixel and all adjacent same colored pixels with C.

For example, given the following matrix, and location pixel of (2, 2), and 'G' for green:

B B W
W W W
W W W
B B B
Becomes

B B G
G G G
G G G
B B B
"""
import unittest

def dimensions(matrix):
    return (len(matrix[0]), len(matrix))

def fill(image, xpos, ypos, color):
    dim = dimensions(image)
    if( xpos >= dim[0] or ypos >= dim[1]):
        raise Exception("coordinates out of bounds of image")
    

class TestChallenge(unittest.TestCase):
    def setUp(self):
        self.expected = [
            ['B','B','G'],
            ['G','G','G'],
            ['G','G','G'],
            ['B','B','B']
        ]
        self.input = [
            ['B','B','W'],
            ['W','W','W'],
            ['W','W','W'],
            ['B','B','B']
        ]
    def test_list_eq(self):
        self.assertListEqual(self.input, self.expected)

if __name__ == '__main__' :
    unittest.main()
    input0 = [
        ['B','B','W'],
        ['W','W','W'],
        ['W','W','W'],
        ['B','B','B']
    ]
    fill(input0, 2, 3, 'G')