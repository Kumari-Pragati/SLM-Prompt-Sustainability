import unittest
from mbpp_807_code import first_odd

class TestFirstOdd(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(first_odd([]), -1)

    def test_all_even(self):
        self.assertEqual(first_odd([2, 4, 6, 8]), -1)

    def test_first_odd(self):
        self.assertEqual(first_odd([2, 3, 4, 5]), 3)

    def test_last_odd(self):
        self.assertEqual(first_odd([2, 4, 6, 7, 8]), 7)

    def test_multiple_odd(self):
        self.assertEqual(first_odd([2, 3, 4, 5, 7]), 3)

    def test_no_odd(self):
        self.assertEqual(first_odd([2, 4, 6, 8, 10]), -1)
