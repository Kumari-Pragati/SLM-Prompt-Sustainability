import unittest
from mbpp_682_code import mul_list

class TestMulList(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(mul_list([1, 2, 3], [4, 5, 6]), [4, 10, 18])

    def test_empty_lists(self):
        self.assertEqual(mul_list([], []), [])

    def test_single_element_lists(self):
        self.assertEqual(mul_list([1], [2]), [2])
        self.assertEqual(mul_list([2], [1]), [2])

    def test_negative_numbers(self):
        self.assertEqual(mul_list([-1, 2], [3, -4]), [-3, 6])

    def test_zero(self):
        self.assertEqual(mul_list([0, 1], [2, 3]), [0, 0])
