import unittest
from mbpp_784_code import mul_even_odd

class TestMulEvenOdd(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(mul_even_odd([]), -1)

    def test_single_element_list(self):
        self.assertEqual(mul_even_odd([5]), -1)

    def test_even_odd_pair(self):
        self.assertEqual(mul_even_odd([2, 3]), 6)

    def test_odd_even_pair(self):
        self.assertEqual(mul_even_odd([3, 4]), 12)

    def test_multiple_even_odd_pairs(self):
        self.assertEqual(mul_even_odd([2, 3, 4, 5]), 60)

    def test_list_with_no_even_numbers(self):
        self.assertEqual(mul_even_odd([1, 3, 5, 7]), -1)

    def test_list_with_no_odd_numbers(self):
        self.assertEqual(mul_even_odd([2, 4, 6, 8]), -1)

    def test_list_with_all_even_numbers(self):
        self.assertEqual(mul_even_odd([2, 4, 6, 8, 10]), 0)

    def test_list_with_all_odd_numbers(self):
        self.assertEqual(mul_even_odd([1, 3, 5, 7, 9]), 0)
