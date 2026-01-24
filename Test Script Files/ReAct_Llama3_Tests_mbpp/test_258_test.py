import unittest
from mbpp_258_code import count_odd

class TestCountOdd(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(count_odd([]), 0)

    def test_single_even(self):
        self.assertEqual(count_odd([2]), 0)

    def test_single_odd(self):
        self.assertEqual(count_odd([1]), 1)

    def test_multiple_odd(self):
        self.assertEqual(count_odd([1, 3, 5, 7]), 4)

    def test_multiple_even(self):
        self.assertEqual(count_odd([2, 4, 6, 8]), 0)

    def test_mixed(self):
        self.assertEqual(count_odd([1, 2, 3, 4, 5, 6]), 3)

    def test_negative_numbers(self):
        self.assertEqual(count_odd([-1, -2, -3, -4, -5]), 3)

    def test_zero(self):
        self.assertEqual(count_odd([0, 0, 0]), 0)
