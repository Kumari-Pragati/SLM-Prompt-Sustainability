import unittest
from mbpp_129_code import magic_square_test

class TestMagicSquare(unittest.TestCase):
    def test_magic_square(self):
        self.assertTrue(magic_square_test([[1, 2, 3], [8, 9, 4], [7, 6, 5]]))
        self.assertTrue(magic_square_test([[16, 3, 2, 13], [5, 10, 11, 8], [9, 6, 15, 14], [4, 7, 12, 11]]))
        self.assertFalse(magic_square_test([[1, 2, 3], [8, 9, 4], [7, 6, 5], [0]]))
        self.assertFalse(magic_square_test([[1, 2, 3], [8, 9, 4], [7, 6, 5], [1, 2, 3]]))
        self.assertFalse(magic_square_test([[1, 2, 3], [8, 9, 4], [7, 6, 5], [1, 2, 3, 4]]))
        self.assertFalse(magic_square_test([[1, 2], [3, 4]]))
        self.assertFalse(magic_square_test([[1, 2, 3], [8, 9], [7, 6, 5]]))
        self.assertFalse(magic_square_test([[1, 2, 3], [8, 9, 4], [7, 6]]))
        self.assertFalse(magic_square_test([[1, 2, 3], [8, 9, 4], [7, 6, 5], [0, 0, 0]]))
        self.assertFalse(magic_square_test([[1, 2, 3], [8, 9, 4], [7, 6, 5], [1, 2, 3, 4], [1, 2, 3, 4]]))
