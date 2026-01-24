import unittest
from mbpp_289_code import date, timedelta
from calendar import isleap

class TestOddDays(unittest.TestCase):

    def test_odd_days(self):
        test_cases = [
            (1990, 3),
            (2000, 1),
            (2004, 6),
            (2016, 4),
            (2100, 0),
            (2023, 5),
        ]

        for year, expected_result in test_cases:
            result = odd_Days(year)
            self.assertEqual(result, expected_result)

    def test_is_leap_year(self):
        self.assertTrue(isleap(1992))
        self.assertFalse(isleap(1991))
        self.assertTrue(isleap(2000))
        self.assertFalse(isleap(2001))

    def test_odd_days_edge_cases(self):
        self.assertEqual(odd_Days(0), 0)
        self.assertEqual(odd_Days(1), 1)
        self.assertEqual(odd_Days(2), 6)
        self.assertEqual(odd_Days(3), 3)
        self.assertEqual(odd_Days(4), 6)
        self.assertEqual(odd_Days(5), 5)
        self.assertEqual(odd_Days(6), 1)
        self.assertEqual(odd_Days(7), 2)
        self.assertEqual(odd_Days(8), 6)
        self.assertEqual(odd_Days(9), 4)
        self.assertEqual(odd_Days(10), 6)
        self.assertEqual(odd_Days(11), 5)
        self.assertEqual(odd_Days(12), 1)
        self.assertEqual(odd_Days(13), 2)
        self.assertEqual(odd_Days(14), 6)
        self.assertEqual(odd_Days(15), 4)
        self.assertEqual(odd_Days(16), 6)
        self.assertEqual(odd_Days(17), 5)
        self.assertEqual(odd_Days(18), 1)
        self.assertEqual(odd_Days(19), 2)
        self.assertEqual(odd_Days(20), 6)
        self.assertEqual(odd_Days(21), 4)
        self.assertEqual(odd_Days(22), 6)
        self.assertEqual(odd_Days(23), 5)
        self.assertEqual(odd_Days(24), 1)
        self.assertEqual(odd_Days(25), 2)
        self.assertEqual(odd_Days(26), 6)
        self.assertEqual(odd_Days(27), 4)
        self.assertEqual(odd_Days(28), 6)
        self.assertEqual(odd_Days(29), 5)
        self.assertEqual(odd_Days(30), 1)
        self.assertEqual(odd_Days(31), 2)
