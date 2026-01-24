import unittest
from mbpp_784_code import mul_even_odd

class TestMulEvenOdd(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(mul_even_odd([1, 2, 3, 4]), 8)

    def test_typical_case_with_zero(self):
        self.assertEqual(mul_even_odd([0, 2, 3, 4]), 0)

    def test_typical_case_with_negative_numbers(self):
        self.assertEqual(mul_even_odd([-1, -2, -3, -4]), -6)

    def test_typical_case_with_mixed_numbers(self):
        self.assertEqual(mul_even_odd([1, -2, 3, -4]), -6)

    def test_empty_list(self):
        self.assertEqual(mul_even_odd([]), -1)

    def test_list_with_single_element(self):
        self.assertEqual(mul_even_odd([2]), -1)

    def test_list_with_no_even_numbers(self):
        self.assertEqual(mul_even_odd([1, 3, 5]), -1)

    def test_list_with_no_odd_numbers(self):
        self.assertEqual(mul_even_odd([2, 4, 6]), -1)

    def test_list_with_all_same_numbers(self):
        self.assertEqual(mul_even_odd([2, 2, 2, 2]), -1)
