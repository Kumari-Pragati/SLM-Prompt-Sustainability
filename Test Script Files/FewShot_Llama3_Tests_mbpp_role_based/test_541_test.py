import unittest
from mbpp_541_code import check_abundant

class TestCheckAbundant(unittest.TestCase):
    def test_abundant_number(self):
        self.assertTrue(check_abundant(12))

    def test_deficient_number(self):
        self.assertFalse(check_abundant(15))

    def test_perfect_number(self):
        self.assertTrue(check_abundant(6))

    def test_prime_number(self):
        self.assertFalse(check_abundant(7))

    def test_edge_case(self):
        self.assertFalse(check_abundant(1))

    def test_edge_case_2(self):
        self.assertFalse(check_abundant(2))
