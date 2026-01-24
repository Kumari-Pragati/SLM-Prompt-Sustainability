import unittest
from mbpp_289_code import odd_Days

class TestOddDays(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(odd_Days(2022), 0)
        self.assertEqual(odd_Days(2023), 1)
        self.assertEqual(odd_Days(2024), 0)
        self.assertEqual(odd_Days(2025), 1)

    def test_leap_year(self):
        self.assertEqual(odd_Days(2000), 0)
        self.assertEqual(odd_Days(2004), 0)
        self.assertEqual(odd_Days(2008), 0)

    def test_non_leap_year(self):
        self.assertEqual(odd_Days(1999), 1)
        self.assertEqual(odd_Days(2002), 1)
        self.assertEqual(odd_Days(2006), 1)

    def test_edge_cases(self):
        self.assertEqual(odd_Days(0), 0)
        self.assertEqual(odd_Days(1), 1)
        self.assertEqual(odd_Days(99), 1)
        self.assertEqual(odd_Days(100), 0)
        self.assertEqual(odd_Days(400), 0)
        self.assertEqual(odd_Days(1000), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            odd_Days('a')
        with self.assertRaises(TypeError):
            odd_Days(None)
