import unittest
from mbpp_611_code import max_of_nth

class TestMaxOfNth(unittest.TestCase):

    def test_typical_case(self):
        test_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = 2
        self.assertEqual(max_of_nth(test_list, N), 8)

    def test_single_element(self):
        test_list = [[1]]
        N = 0
        self.assertEqual(max_of_nth(test_list, N), 1)

    def test_negative_numbers(self):
        test_list = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]
        N = 2
        self.assertEqual(max_of_nth(test_list, N), -2)

    def test_zero(self):
        test_list = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        N = 1
        self.assertEqual(max_of_nth(test_list, N), 0)

    def test_empty_list(self):
        test_list = []
        N = 0
        with self.assertRaises(ValueError):
            max_of_nth(test_list, N)

    def test_invalid_N(self):
        test_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = -1
        with self.assertRaises(IndexError):
            max_of_nth(test_list, N)
