import unittest
from mbpp_289_code import odd_Days

class TestOddDays(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(odd_Days(2023), 3)

    def test_leap_year(self):
        self.assertEqual(odd_Days(2000), 0)

    def test_non_leap_year(self):
        self.assertEqual(odd_Days(2022), 4)

    def test_boundary_conditions(self):
        self.assertEqual(odd_Days(0), 0)
        self.assertEqual(odd_Days(100), 1)
        self.assertEqual(odd_Days(400), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            odd_Days('2023')
        with self.assertRaises(ValueError):
            odd_Days(-2023)
