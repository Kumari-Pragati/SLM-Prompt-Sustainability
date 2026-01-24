import unittest
from mbpp_129_code import magic_square_test

class TestMagicSquare(unittest.TestCase):
    def test_magic_square_1(self):
        self.assertTrue(magic_square_test([[1, 2, 3], [8, 9, 4], [7, 6, 5]]))

    def test_magic_square_2(self):
        self.assertTrue(magic_square_test([[16, 3, 2, 13], [5, 10, 11, 8], [9, 6, 7, 12], [4, 15, 14, 1]]))

    def test_magic_square_3(self):
        self.assertFalse(magic_square_test([[1, 2, 3], [8, 9, 4], [7, 6, 5], [0]]))

    def test_magic_square_4(self):
        self.assertFalse(magic_square_test([[1, 2, 3], [8, 9, 4], [7, 6, 5], [1, 2, 3]]))

    def test_magic_square_5(self):
        self.assertFalse(magic_square_test([[1, 2, 3], [8, 9, 4], [7, 6, 5], [1, 2, 3], [4, 5, 6]]))

    def test_magic_square_6(self):
        self.assertFalse(magic_square_test([[1, 2, 3], [8, 9, 4], [7, 6, 5], [1, 2, 3], [4, 5, 6], [0]]))
