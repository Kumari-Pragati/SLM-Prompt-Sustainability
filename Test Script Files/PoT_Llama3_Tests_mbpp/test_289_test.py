import unittest
from mbpp_289_code import odd_Days

class TestOddDays(unittest.TestCase):

    def test_typical(self):
        self.assertEqual(odd_Days(1), 1)
        self.assertEqual(odd_Days(2), 0)
        self.assertEqual(odd_Days(3), 1)
        self.assertEqual(odd_Days(4), 0)
        self.assertEqual(odd_Days(5), 1)
        self.assertEqual(odd_Days(6), 0)
        self.assertEqual(odd_Days(7), 1)

    def test_leap_year(self):
        self.assertEqual(odd_Days(2020), 0)
        self.assertEqual(odd_Days(2024), 0)
        self.assertEqual(odd_Days(2028), 0)

    def test_non_leap_year(self):
        self.assertEqual(odd_Days(2019), 1)
        self.assertEqual(odd_Days(2021), 1)
        self.assertEqual(odd_Days(2022), 0)
        self.assertEqual(odd_Days(2023), 1)

    def test_edge(self):
        self.assertEqual(odd_Days(0), 0)
        self.assertEqual(odd_Days(100), 1)
        self.assertEqual(odd_Days(400), 0)
        self.assertEqual(odd_Days(1000), 1)
