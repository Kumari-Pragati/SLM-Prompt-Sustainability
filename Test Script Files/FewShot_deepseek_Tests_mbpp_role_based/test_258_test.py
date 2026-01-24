import unittest
from mbpp_258_code import count_odd

class TestCountOdd(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(count_odd([1, 2, 3, 4, 5]), 3)

    def test_empty_list(self):
        self.assertEqual(count_odd([]), 0)

    def test_all_even_numbers(self):
        self.assertEqual(count_odd([2, 4, 6, 8]), 0)

    def test_all_odd_numbers(self):
        self.assertEqual(count_odd([1, 3, 5, 7]), 4)

    def test_mixed_numbers(self):
        self.assertEqual(count_odd([1, 2, 3, 4, 5, 6, 7, 8]), 4)

    def test_large_numbers(self):
        self.assertEqual(count_odd(list(range(1, 10001))), 5000)

    def test_negative_numbers(self):
        self.assertEqual(count_odd([-1, -2, -3, -4, -5]), 3)

    def test_negative_and_positive_numbers(self):
        self.assertEqual(count_odd([-1, 2, -3, 4, -5]), 3)
