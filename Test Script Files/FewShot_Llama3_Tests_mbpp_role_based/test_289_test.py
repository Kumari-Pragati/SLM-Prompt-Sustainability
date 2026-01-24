import unittest
from mbpp_289_code import odd_Days

class TestOddDays(unittest.TestCase):
    def test_leap_year(self):
        self.assertEqual(odd_Days(2020), 3)

    def test_non_leap_year(self):
        self.assertEqual(odd_Days(2019), 1)

    def test_century_year(self):
        self.assertEqual(odd_Days(400), 0)

    def test_non_century_year(self):
        self.assertEqual(odd_Days(300), 1)

    def test_zero(self):
        self.assertEqual(odd_Days(0), 0)

    def test_negative(self):
        with self.assertRaises(TypeError):
            odd_Days(-1)
