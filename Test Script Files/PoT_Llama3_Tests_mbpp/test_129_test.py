import unittest
from mbpp_129_code import magic_square_test

class TestMagicSquare(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(magic_square_test([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

    def test_edge_case(self):
        self.assertTrue(magic_square_test([[1, 2], [3, 4]]))

    def test_edge_case2(self):
        self.assertTrue(magic_square_test([[1, 2, 3, 4], [5, 6, 7, 8]]))

    def test_edge_case3(self):
        self.assertTrue(magic_square_test([[1, 2, 3], [4, 5, 6]]))

    def test_edge_case4(self):
        self.assertTrue(magic_square_test([[1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18]]))

    def test_invalid_input1(self):
        with self.assertRaises(TypeError):
            magic_square_test('')

    def test_invalid_input2(self):
        with self.assertRaises(TypeError):
            magic_square_test([1, 2, 3])

    def test_invalid_input3(self):
        with self.assertRaises(TypeError):
            magic_square_test([[1, 2, 3], [4, 5, 6], [7, 8, 9, 10]])

    def test_invalid_input4(self):
        with self.assertRaises(TypeError):
            magic_square_test([[1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11, 12]])
