import unittest
from mbpp_258_code import count_odd

class TestCountOdd(unittest.TestCase):

    def test_count_odd_positive(self):
        self.assertEqual(count_odd([1, 2, 3, 4, 5]), 3)

    def test_count_odd_negative(self):
        self.assertEqual(count_odd([2, 4, 6, 8, 10]), 0)

    def test_count_odd_mixed(self):
        self.assertEqual(count_odd([1, 2, 3, 4, 5, 6, 7, 8, 9]), 5)

    def test_count_odd_empty(self):
        self.assertEqual(count_odd([]), 0)

    def test_count_odd_single_element(self):
        self.assertEqual(count_odd([7]), 1)

    def test_count_odd_single_even(self):
        self.assertEqual(count_odd([2]), 0)
