import unittest
from mbpp_289_code import odd_Days

class TestOddDays(unittest.TestCase):

    def test_simple_years(self):
        self.assertEqual(odd_Days(1900), 3)
        self.assertEqual(odd_Days(2000), 1)
        self.assertEqual(odd_Days(2016), 4)

    def test_edge_cases(self):
        self.assertEqual(odd_Days(0), 5)
        self.assertEqual(odd_Days(1), 6)
        self.assertEqual(odd_Days(365), 6)
        self.assertEqual(odd_Days(366), 1)

    def test_leap_years(self):
        self.assertEqual(odd_Days(1600), 3)
        self.assertEqual(odd_Days(2400), 5)
        self.assertEqual(odd_Days(2404), 6)
        self.assertEqual(odd_Days(2408), 3)

    def test_complex_cases(self):
        self.assertEqual(odd_Days(1700), 3)
        self.assertEqual(odd_Days(2800), 5)
        self.assertEqual(odd_Days(4000), 1)
        self.assertEqual(odd_Days(4004), 6)
