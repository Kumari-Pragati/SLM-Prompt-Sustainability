import unittest
from mbpp_56_code import check

class TestCheckFunction(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check(15))

    def test_edge_case_zero(self):
        self.assertFalse(check(0))

    def test_edge_case_negative(self):
        self.assertFalse(check(-1))

    def test_edge_case_large_number(self):
        self.assertFalse(check(1000000))

    def test_corner_case_even_number(self):
        self.assertFalse(check(12))

    def test_corner_case_odd_number_with_1_as_last_digit(self):
        self.assertTrue(check(21))

    def test_corner_case_odd_number_with_9_as_last_digit(self):
        self.assertFalse(check(29))
