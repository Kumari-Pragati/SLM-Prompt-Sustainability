import unittest
from mbpp_221_code import first_even

class TestFirstEven(unittest.TestCase):
    def test_first_even_in_list(self):
        self.assertEqual(first_even([2, 4, 6, 8]), 2)

    def test_first_even_in_list_with_multiple_evens(self):
        self.assertEqual(first_even([2, 4, 6, 8, 10]), 2)

    def test_first_even_in_list_with_no_evens(self):
        self.assertEqual(first_even([1, 3, 5, 7]), -1)

    def test_first_even_in_list_with_mixed_evens_and_odds(self):
        self.assertEqual(first_even([2, 4, 1, 3, 5, 6]), 2)

    def test_first_even_in_empty_list(self):
        self.assertEqual(first_even([]), -1)
