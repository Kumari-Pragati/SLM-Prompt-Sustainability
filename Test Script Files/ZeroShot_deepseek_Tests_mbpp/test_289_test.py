import unittest
from mbpp_289_code import odd_Days

class TestOddDays(unittest.TestCase):

    def test_odd_Days(self):
        self.assertEqual(odd_Days(1980), 1)
        self.assertEqual(odd_Days(2000), 1)
        self.assertEqual(odd_Days(1999), 0)
        self.assertEqual(odd_Days(2001), 2)
        self.assertEqual(odd_Days(1900), 1)
        self.assertEqual(odd_Days(2002), 3)
        self.assertEqual(odd_Days(1970), 3)
        self.assertEqual(odd_Days(2020), 2)
        self.assertEqual(odd_Days(2021), 3)
        self.assertEqual(odd_Days(2022), 4)
        self.assertEqual(odd_Days(2023), 5)
        self.assertEqual(odd_Days(2024), 6)
        self.assertEqual(odd_Days(2025), 0)
