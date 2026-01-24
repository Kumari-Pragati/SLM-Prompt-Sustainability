import unittest
from mbpp_348_code import find_ways

class TestFindWays(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(find_ways(4), 1)

    def test_edge_case_M_even(self):
        self.assertEqual(find_ways(6), 1)

    def test_edge_case_M_odd(self):
        self.assertEqual(find_ways(5), 1)

    def test_edge_case_M_zero(self):
        with self.assertRaises(ZeroDivisionError):
            find_ways(0)

    def test_edge_case_M_negative(self):
        with self.assertRaises(ValueError):
            find_ways(-1)
