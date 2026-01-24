import unittest
from mbpp_541_code import check_abundant

class TestCheckAbundant(unittest.TestCase):
    def test_typical_abundant(self):
        self.assertTrue(check_abundant(12))
        self.assertTrue(check_abundant(28))
        self.assertTrue(check_abundant(496))

    def test_typical_not_abundant(self):
        self.assertFalse(check_abundant(11))
        self.assertFalse(check_abundant(13))
        self.assertFalse(check_abundant(19))

    def test_edge_cases(self):
        self.assertTrue(check_abundant(1))
        self.assertTrue(check_abundant(2))
        self.assertFalse(check_abundant(0))
        self.assertFalse(check_abundant(-1))

    def test_boundary_cases(self):
        self.assertTrue(check_abundant(math.ceil(math.sqrt(2**31)) - 1))
        self.assertFalse(check_abundant(math.ceil(math.sqrt(2**31))))
