import unittest
from mbpp_258_code import count_odd

class TestCountOdd(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(count_odd([]), 0)

    def test_single_even_number(self):
        self.assertEqual(count_odd([2]), 0)

    def test_single_odd_number(self):
        self.assertEqual(count_odd([1]), 1)

    def test_multiple_even_numbers(self):
        self.assertEqual(count_odd([2, 4, 6]), 0)

    def test_multiple_odd_numbers(self):
        self.assertEqual(count_odd([1, 3, 5]), 3)

    def test_mixed_numbers(self):
        self.assertEqual(count_odd([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), 5)
