import unittest
from mbpp_807_code import first_odd

class TestFirstOdd(unittest.TestCase):

    def test_first_odd_positive(self):
        self.assertEqual(first_odd([2, 4, 6, 8, 10]), -1)

    def test_first_odd_negative(self):
        self.assertEqual(first_odd([2, 4, 6, 8, -10]), -1)

    def test_first_odd_mixed(self):
        self.assertEqual(first_odd([2, 4, 6, 8, -10, 15]), 15)

    def test_first_odd_empty(self):
        self.assertEqual(first_odd([]), -1)

    def test_first_odd_single_element(self):
        self.assertEqual(first_odd([2]), -1)

    def test_first_odd_all_odds(self):
        self.assertEqual(first_odd([3, 5, 7, 9]), 3)
