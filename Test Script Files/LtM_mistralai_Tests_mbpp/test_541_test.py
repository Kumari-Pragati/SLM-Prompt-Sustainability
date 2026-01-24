import unittest
from mbpp_541_code import check_abundant

class TestCheckAbundant(unittest.TestCase):

    def test_simple_abundant(self):
        self.assertTrue(check_abundant(12))
        self.assertTrue(check_abundant(28))

    def test_simple_not_abundant(self):
        self.assertFalse(check_abundant(10))
        self.assertFalse(check_abundant(15))

    def test_edge_cases(self):
        self.assertTrue(check_abundant(math.ceil(math.sqrt(2**31))))
        self.assertFalse(check_abundant(math.floor(math.sqrt(2**31))))

    def test_boundary_cases(self):
        self.assertTrue(check_abundant(1))
        self.assertTrue(check_abundant(2))
        self.assertFalse(check_abundant(0))
