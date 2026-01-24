import unittest
from mbpp_682_code import mul_list

class TestMulList(unittest.TestCase):

    def test_empty_lists(self):
        self.assertListEqual(mul_list([], []), [])
        self.assertListEqual(mul_list([], [1]), [])
        self.assertListEqual(mul_list([1], []), [])

    def test_single_element_lists(self):
        self.assertListEqual(mul_list([1], [2]), [2])
        self.assertListEqual(mul_list([2], [1]), [2])

    def test_positive_numbers(self):
        self.assertListEqual(mul_list([1, 2, 3], [4, 5, 6]), [4, 10, 18])
        self.assertListEqual(mul_list([4, 5, 6], [1, 2, 3]), [4, 10, 18])

    def test_negative_numbers(self):
        self.assertListEqual(mul_list([-1, -2, -3], [-4, -5, -6]), [4, 10, 18])
        self.assertListEqual(mul_list([-4, -5, -6], [-1, -2, -3]), [4, 10, 18])

    def test_zero(self):
        self.assertListEqual(mul_list([0, 1, 2], [3, 4, 5]), [0, 0, 0])
        self.assertListEqual(mul_list([3, 4, 5], [0, 1, 2]), [0, 0, 0])

    def test_mixed_numbers(self):
        self.assertListEqual(mul_list([1, -2, 3], [4, -5, 6]), [-4, 10, -18])
        self.assertListEqual(mul_list([4, -5, 6], [1, -2, 3]), [-4, 10, -18])

    def test_list_lengths(self):
        self.assertListEqual(mul_list([1, 2, 3], [4]), [4, 8, 12])
        self.assertListEqual(mul_list([1, 2, 3], [4, 5]), [4, 10, 15])
        self.assertListEqual(mul_list([1, 2, 3], [4, 5, 6]), [4, 10, 15, 18])

        self.assertListEqual(mul_list([1], [4, 5]), [4, 5])
        self.assertListEqual(mul_list([1, 2], [4, 5]), [4, 10])
        self.assertListEqual(mul_list([1, 2, 3], [4, 5]), [4, 10, 15])

    def test_error_cases(self):
        with self.assertRaises(TypeError):
            mul_list('a', 'b')
        with self.assertRaises(TypeError):
            mul_list([1], 'b')
        with self.assertRaises(TypeError):
            mul_list('a', [1])
