import unittest
from mbpp_682_code import mul_list

class TestMulList(unittest.TestCase):

    def test_empty_lists(self):
        self.assertEqual(mul_list([], []), [])

    def test_single_element_lists(self):
        self.assertEqual(mul_list([1], [2]), [2])
        self.assertEqual(mul_list([1, 2], [3]), [3, 6])

    def test_lists_of_different_lengths(self):
        self.assertEqual(mul_list([1, 2, 3], [4]), [4, 8, 12])
        self.assertEqual(mul_list([1, 2, 3, 4], [5]), [5, 10, 15, 20])

    def test_lists_with_zero(self):
        self.assertEqual(mul_list([1, 2, 3], [0]), [0, 0, 0])
        self.assertEqual(mul_list([1, 2, 3, 4], [0]), [0, 0, 0, 0])

    def test_lists_with_negative_numbers(self):
        self.assertEqual(mul_list([-1, 2, 3], [4]), [4, -8, 12])
        self.assertEqual(mul_list([1, 2, 3, 4], [-5]), [-5, -10, -15, -20])

    def test_lists_with_mixed_signs(self):
        self.assertEqual(mul_list([-1, 2, 3], [-4]), [4, -8, 12])
        self.assertEqual(mul_list([1, 2, 3, 4], [-5]), [-5, -10, -15, -20])
