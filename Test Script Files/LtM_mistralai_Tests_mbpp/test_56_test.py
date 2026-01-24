import unittest
from mbpp_56_code import check

class TestCheckFunction(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertTrue(check(15))
        self.assertTrue(check(37))
        self.assertTrue(check(20))

    def test_edge_and_boundary_conditions(self):
        self.assertFalse(check(0))
        self.assertFalse(check(1))
        self.assertFalse(check(2))
        self.assertTrue(check(99))
        self.assertTrue(check(999))
        self.assertFalse(check(1000))

    def test_complex_inputs(self):
        self.assertFalse(check(-1))
        self.assertTrue(check(2147483647))  # max int value
        self.assertFalse(check(2**31))  # max int value + 1
        self.assertTrue(check(2**31 - 1))  # max int value - 1
