import unittest
from mbpp_221_code import first_even

class TestFirstEven(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(first_even([]), -1)

    def test_no_even_numbers(self):
        self.assertEqual(first_even([1, 3, 5, 7]), -1)

    def test_first_even(self):
        self.assertEqual(first_even([2, 4, 6, 8]), 2)

    def test_first_even_at_end(self):
        self.assertEqual(first_even([1, 3, 5, 6]), 6)

    def test_first_even_at_start(self):
        self.assertEqual(first_even([2, 4, 6, 8, 10]), 2)

    def test_first_even_at_middle(self):
        self.assertEqual(first_even([1, 3, 4, 5, 6]), 4)

    def test_first_even_with_negative_numbers(self):
        self.assertEqual(first_even([-2, 1, 3, 4, 5]), -2)

    def test_first_even_with_mixed_numbers(self):
        self.assertEqual(first_even([1, 2, 3, 4, 5, 6]), 1)
