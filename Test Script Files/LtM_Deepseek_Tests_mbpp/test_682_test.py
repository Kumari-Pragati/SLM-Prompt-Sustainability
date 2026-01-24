import unittest
from mbpp_682_code import mul_list

class TestMulList(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(mul_list([1, 2, 3], [4, 5, 6]), [4, 10, 18])

    def test_empty_lists(self):
        self.assertEqual(mul_list([], []), [])

    def test_one_empty_list(self):
        self.assertEqual(mul_list([1, 2, 3], []), [])
        self.assertEqual(mul_list([], [4, 5, 6]), [])

    def test_negative_numbers(self):
        self.assertEqual(mul_list([-1, 2, -3], [4, -5, 6]), [-4, -10, -18])

    def test_zero_numbers(self):
        self.assertEqual(mul_list([0, 2, 3], [4, 5, 6]), [0, 10, 18])

    def test_large_numbers(self):
        self.assertEqual(mul_list([1000000000, 2000000000], [3000000000, 4000000000]), [3000000000000000000, 8000000000000000000])
