import unittest
from mbpp_603_code import get_ludic

class TestGetLudic(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(get_ludic(5), [1, 3, 5])

    def test_edge_case_small(self):
        self.assertEqual(get_ludic(1), [1])

    def test_edge_case_large(self):
        self.assertEqual(get_ludic(100), [1, 7, 9, 23, 29, 41, 59, 71])

    def test_boundary_case_zero(self):
        self.assertEqual(get_ludic(0), [])

    def test_boundary_case_negative(self):
        self.assertRaises(ValueError, get_ludic, -1)
