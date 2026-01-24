import unittest
from mbpp_129_code import magic_square_test

class TestMagicSquare(unittest.TestCase):
    def test_valid_magic_square(self):
        my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertTrue(magic_square_test(my_matrix))

    def test_invalid_magic_square(self):
        my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 10]]
        self.assertFalse(magic_square_test(my_matrix))

    def test_edge_case_magic_square(self):
        my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertTrue(magic_square_test(my_matrix))

    def test_empty_magic_square(self):
        my_matrix = []
        self.assertFalse(magic_square_test(my_matrix))

    def test_single_element_magic_square(self):
        my_matrix = [[1]]
        self.assertTrue(magic_square_test(my_matrix))
