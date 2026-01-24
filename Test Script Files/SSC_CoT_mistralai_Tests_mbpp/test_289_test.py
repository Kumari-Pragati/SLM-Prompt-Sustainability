import unittest
from mbpp_289_code import odd_Days

class TestOddDays(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(odd_Days(2000), 6)
        self.assertEqual(odd_Days(2400), 4)
        self.assertEqual(odd_Days(2500), 1)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(odd_Days(0), 6)
        self.assertEqual(odd_Days(1), 1)
        self.assertEqual(odd_Days(3), 2)
        self.assertEqual(odd_Days(100), 3)
        self.assertEqual(odd_Days(399), 6)
        self.assertEqual(odd_Days(400), 3)
        self.assertEqual(odd_Days(401), 6)
        self.assertEqual(odd_Days(999), 4)
        self.assertEqual(odd_Days(1000), 1)
        self.assertEqual(odd_Days(1999), 2)
        self.assertEqual(odd_Days(2001), 6)
        self.assertEqual(odd_Days(3999), 6)
        self.assertEqual(odd_Days(4000), 3)
        self.assertEqual(odd_Days(4001), 6)

    def test_leap_years(self):
        self.assertEqual(odd_Days(1600), 3)
        self.assertEqual(odd_Days(1700), 6)
        self.assertEqual(odd_Days(1800), 3)
        self.assertEqual(odd_Days(1900), 6)
        self.assertEqual(odd_Days(2000), 6)
        self.assertEqual(odd_Days(2100), 1)
        self.assertEqual(odd_Days(2200), 6)
        self.assertEqual(odd_Days(2300), 3)
        self.assertEqual(odd_Days(2400), 4)
        self.assertEqual(odd_Days(2500), 1)
