import unittest
from mbpp_784_code import mul_even_odd

class TestMulEvenOdd(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(mul_even_odd([]), -1)

    def test_single_element_list(self):
        self.assertEqual(mul_even_odd([5]), -1)

    def test_list_with_no_even_numbers(self):
        self.assertEqual(mul_even_odd([1, 3, 5, 7]), -1)

    def test_list_with_no_odd_numbers(self):
        self.assertEqual(mul_even_odd([2, 4, 6, 8]), -1)

    def test_list_with_one_even_and_one_odd(self):
        self.assertEqual(mul_even_odd([2, 3]), 6)

    def test_list_with_multiple_even_and_odd(self):
        self.assertEqual(mul_even_odd([2, 4, 6, 3, 5, 7]), 24)

    def test_list_with_duplicates(self):
        self.assertEqual(mul_even_odd([2, 2, 4, 4, 6, 6, 3, 3, 5, 5, 7, 7]), 24)
