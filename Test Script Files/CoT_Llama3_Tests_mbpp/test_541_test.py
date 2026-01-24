import unittest
from mbpp_541_code import check_abundant

class TestCheckAbundant(unittest.TestCase):

    def test_abundant(self):
        self.assertTrue(check_abundant(12))
        self.assertTrue(check_abundant(24))
        self.assertTrue(check_abundant(36))

    def test_not_abundant(self):
        self.assertFalse(check_abundant(1))
        self.assertFalse(check_abundant(2))
        self.assertFalse(check_abundant(3))

    def test_edge_cases(self):
        self.assertFalse(check_abundant(0))
        self.assertFalse(check_abundant(4))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_abundant('a')
