import unittest
from mbpp_289_code import odd_Days

class TestOddDays(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(odd_Days(1), 1)
        self.assertEqual(odd_Days(100), 3)
        self.assertEqual(odd_Days(400), 0)
        self.assertEqual(odd_Days(500), 1)

    def test_edge_cases(self):
        self.assertEqual(odd_Days(0), 0)
        self.assertEqual(odd_Days(365), 1)
        self.assertEqual(odd_Days(730), 2)

    def test_boundary_conditions(self):
        self.assertEqual(odd_Days(366), 0)
        self.assertEqual(odd_Days(731), 1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            odd_Days('abc')
        with self.assertRaises(ValueError):
            odd_Days(-1)
