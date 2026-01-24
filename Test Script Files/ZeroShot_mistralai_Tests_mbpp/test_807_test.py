import unittest
from mbpp_807_code import first_odd

class TestFirstOdd(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(first_odd([]), -1)

    def test_all_even_numbers(self):
        self.assertEqual(first_odd([2, 4, 6]), -1)

    def test_single_odd_number(self):
        self.assertEqual(first_odd([1, 2, 3]), 1)

    def test_single_even_number(self):
        self.assertEqual(first_odd([2, 3]), -1)

    def test_multiple_odd_numbers(self):
        self.assertEqual(first_odd([1, 3, 5, 2]), 1)

    def test_multiple_even_numbers(self):
        self.assertEqual(first_odd([2, 4, 6, 8]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(first_odd([1, 2, 3, 4, 5, 6, 7]), 1)
