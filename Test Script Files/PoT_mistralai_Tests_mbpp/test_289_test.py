import unittest
from mbpp_289_code import odd_Days

class TestOddDays(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(odd_Days(2016), 1)
        self.assertEqual(odd_Days(2017), 3)
        self.assertEqual(odd_Days(2018), 5)
        self.assertEqual(odd_Days(2019), 6)
        self.assertEqual(odd_Days(2020), 0)
        self.assertEqual(odd_Days(2021), 1)
        self.assertEqual(odd_Days(2022), 3)
        self.assertEqual(odd_Days(2023), 5)
        self.assertEqual(odd_Days(2024), 6)
        self.assertEqual(odd_Days(2025), 0)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(odd_Days(0), 6)
        self.assertEqual(odd_Days(1), 0)
        self.assertEqual(odd_Days(2), 1)
        self.assertEqual(odd_Days(3), 2)
        self.assertEqual(odd_Days(4), 3)
        self.assertEqual(odd_Days(5), 4)
        self.assertEqual(odd_Days(6), 5)
        self.assertEqual(odd_Days(7), 6)
        self.assertEqual(odd_Days(8), 0)
        self.assertEqual(odd_Days(9), 1)
        self.assertEqual(odd_Days(100), 5)
        self.assertEqual(odd_Days(101), 6)
        self.assertEqual(odd_Days(399), 6)
        self.assertEqual(odd_Days(400), 0)
        self.assertEqual(odd_Days(401), 1)
        self.assertEqual(odd_Days(999), 5)
        self.assertEqual(odd_Days(1000), 6)
