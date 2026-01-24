import unittest
from mbpp_289_code import odd_Days

class TestOddDays(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(odd_Days(2016), 1)
        self.assertEqual(odd_Days(2000), 0)
        self.assertEqual(odd_Days(1900), 3)
        self.assertEqual(odd_Days(2400), 6)

    def test_zero_and_negative_numbers(self):
        self.assertEqual(odd_Days(0), 0)
        self.assertEqual(odd_Days(-1), 6)
        self.assertEqual(odd_Days(-2000), 5)
        self.assertEqual(odd_Days(-4000), 1)

    def test_edge_cases(self):
        self.assertEqual(odd_Days(399), 3)
        self.assertEqual(odd_Days(400), 0)
        self.assertEqual(odd_Days(3999), 6)
        self.assertEqual(odd_Days(4000), 0)
