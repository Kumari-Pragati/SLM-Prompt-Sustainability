import unittest
from mbpp_541_code import check_abundant

class TestCheckAbundant(unittest.TestCase):

    def test_normal(self):
        self.assertTrue(check_abundant(28))
        self.assertTrue(check_abundant(12))
        self.assertTrue(check_abundant(72))

    def test_edge_and_boundary(self):
        self.assertFalse(check_abundant(1))
        self.assertFalse(check_abundant(2))
        self.assertFalse(check_abundant(18))
        self.assertTrue(check_abundant(19))
        self.assertTrue(check_abundant(20))
        self.assertFalse(check_abundant(21))
        self.assertTrue(check_abundant(22))
        self.assertTrue(check_abundant(100))
        self.assertTrue(check_abundant(101))
        self.assertFalse(check_abundant(102))

    def test_special_cases(self):
        self.assertTrue(check_abundant(8))
        self.assertTrue(check_abundant(20))
        self.assertTrue(check_abundant(28))
