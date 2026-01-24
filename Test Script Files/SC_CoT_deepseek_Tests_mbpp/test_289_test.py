import unittest
from mbpp_289_code import odd_Days

class TestOddDays(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(odd_Days(2000), 0)
        self.assertEqual(odd_Days(2023), 3)

    def test_boundary_conditions(self):
        self.assertEqual(odd_Days(0), 0)
        self.assertEqual(odd_Days(100), 1)
        self.assertEqual(odd_Days(400), 0)

    def test_edge_cases(self):
        self.assertEqual(odd_Days(99), 1)
        self.assertEqual(odd_Days(399), 3)
        self.assertEqual(odd_Days(401), 0)
        self.assertEqual(odd_Days(999), 1)
        self.assertEqual(odd_Days(1000), 2)
        self.assertEqual(odd_Days(1001), 3)
        self.assertEqual(odd_Days(1999), 3)
        self.assertEqual(odd_Days(2001), 4)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            odd_Days('2023')
        with self.assertRaises(ValueError):
            odd_Days(-2023)
