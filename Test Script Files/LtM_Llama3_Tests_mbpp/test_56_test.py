import unittest
from mbpp_56_code import check

class TestCheckFunction(unittest.TestCase):
    def test_simple_positive(self):
        self.assertTrue(check(1))
        self.assertTrue(check(2))
        self.assertTrue(check(3))

    def test_simple_negative(self):
        self.assertFalse(check(-1))
        self.assertFalse(check(-2))
        self.assertFalse(check(-3))

    def test_edge_case_zero(self):
        self.assertFalse(check(0))

    def test_edge_case_one(self):
        self.assertTrue(check(1))

    def test_edge_case_large(self):
        self.assertTrue(check(1000))

    def test_edge_case_negative_large(self):
        self.assertFalse(check(-1000))

    def test_edge_case_negative_small(self):
        self.assertFalse(check(-1))

    def test_edge_case_positive_large(self):
        self.assertTrue(check(1000))

    def test_edge_case_positive_small(self):
        self.assertTrue(check(1))
