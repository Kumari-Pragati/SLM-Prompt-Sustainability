import unittest
from mbpp_20_code import is_woodall

class TestIsWoodall(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(is_woodall(1))
        self.assertTrue(is_woodall(3))
        self.assertTrue(is_woodall(15))
        self.assertTrue(is_woodall(511))

    def test_edge_cases(self):
        self.assertFalse(is_woodall(0))
        self.assertFalse(is_woodall(2))
        self.assertFalse(is_woodall(4))
        self.assertFalse(is_woodall(6))

    def test_explicitly_handled_error_cases(self):
        self.assertFalse(is_woodall(-1))
        self.assertFalse(is_woodall(1.5))
        self.assertFalse(is_woodall('15'))
