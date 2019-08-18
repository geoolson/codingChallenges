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

class ColorFill():
    def __init__(self, matrix):
        self.image = matrix
        self.dim = (len(matrix[0]), len(matrix))

    def _fill(self, xpos, ypos, color, ogcolor):
        if(xpos < 0 or ypos < 0):
            return
        if( xpos >= self.dim[1] or ypos >= self.dim[0]):
            return
        elif( self.image[xpos][ypos] == ogcolor ):
            self.image[xpos][ypos] = color
            self._fill(xpos-1, ypos, color, ogcolor)
            self._fill(xpos+1, ypos, color, ogcolor)
            self._fill(xpos, ypos-1, color, ogcolor)
            self._fill(xpos, ypos+1, color, ogcolor)
        else:
            return

    def fill(self, xpos, ypos, color):
        if( xpos >= self.dim[0] or ypos >= self.dim[1]):
            raise Exception("coordinates out of bounds of image")
        ogColor = self.image[xpos][ypos]
        self._fill( xpos, ypos, color, ogColor)
        return self.image

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
        colorFill = ColorFill(self.input)
        self.result = colorFill.fill(2, 2, 'G')

    def test_list_eq(self):
        self.assertListEqual(self.result, self.expected)

if __name__ == '__main__' :
    unittest.main()