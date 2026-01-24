import unittest
from mbpp_289_code import odd_Days

class TestOddDays(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(odd_Days(1), 1)
        self.assertEqual(odd_Days(2), 0)
        self.assertEqual(odd_Days(3), 1)
        self.assertEqual(odd_Days(4), 0)
        self.assertEqual(odd_Days(5), 1)
        self.assertEqual(odd_Days(6), 0)
        self.assertEqual(odd_Days(7), 1)
        self.assertEqual(odd_Days(8), 0)
        self.assertEqual(odd_Days(9), 1)
        self.assertEqual(odd_Days(10), 0)

    def test_leap_years(self):
        self.assertEqual(odd_Days(2000), 0)
        self.assertEqual(odd_Days(2004), 0)
        self.assertEqual(odd_Days(2008), 0)
        self.assertEqual(odd_Days(2012), 0)
        self.assertEqual(odd_Days(2016), 0)
        self.assertEqual(odd_Days(2020), 0)

    def test_non_leap_years(self):
        self.assertEqual(odd_Days(1999), 1)
        self.assertEqual(odd_Days(2003), 1)
        self.assertEqual(odd_Days(2007), 1)
        self.assertEqual(odd_Days(2011), 1)
        self.assertEqual(odd_Days(2015), 1)
        self.assertEqual(odd_Days(2019), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            odd_Days("a")
        with self.assertRaises(TypeError):
            odd_Days(None)
        with self.assertRaises(TypeError):
            odd_Days(123.45)
