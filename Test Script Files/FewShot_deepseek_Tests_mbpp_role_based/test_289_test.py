import unittest
from mbpp_289_code import odd_Days

class TestOddDays(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(odd_Days(200), 1)

    def test_boundary_conditions(self):
        self.assertEqual(odd_Days(0), 0)
        self.assertEqual(odd_Days(365), 1)
        self.assertEqual(odd_Days(730), 0)

    def test_edge_conditions(self):
        self.assertEqual(odd_Days(366), 2)
        self.assertEqual(odd_Days(731), 3)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            odd_Days('200')
        with self.assertRaises(ValueError):
            odd_Days(-200)
