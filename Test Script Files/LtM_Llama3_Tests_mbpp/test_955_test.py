import unittest
from mbpp_955_code import is_abundant

class TestIsAbundant(unittest.TestCase):
    def test_simple_positive(self):
        self.assertTrue(is_abundant(12))
    def test_simple_negative(self):
        self.assertFalse(is_abundant(-12))
    def test_simple_zero(self):
        self.assertFalse(is_abundant(0))
    def test_edge_one(self):
        self.assertFalse(is_abundant(1))
    def test_edge_two(self):
        self.assertTrue(is_abundant(2))
    def test_edge_three(self):
        self.assertFalse(is_abundant(3))
    def test_edge_four(self):
        self.assertTrue(is_abundant(4))
    def test_edge_five(self):
        self.assertFalse(is_abundant(5))
    def test_edge_six(self):
        self.assertTrue(is_abundant(6))
    def test_edge_seven(self):
        self.assertFalse(is_abundant(7))
    def test_edge_eight(self):
        self.assertTrue(is_abundant(8))
    def test_edge_nine(self):
        self.assertFalse(is_abundant(9))
    def test_edge_ten(self):
        self.assertTrue(is_abundant(10))
    def test_edge_eleven(self):
        self.assertFalse(is_abundant(11))
    def test_edge_twelve(self):
        self.assertTrue(is_abundant(12))
    def test_edge_fifteen(self):
        self.assertFalse(is_abundant(15))
    def test_edge_twenty(self):
        self.assertTrue(is_abundant(20))
    def test_edge_twentyfive(self):
        self.assertFalse(is_abundant(25))
    def test_edge_thirty(self):
        self.assertTrue(is_abundant(30))
    def test_edge_fifty(self):
        self.assertFalse(is_abundant(50))
    def test_edge_sixty(self):
        self.assertTrue(is_abundant(60))
    def test_edge_seventy(self):
        self.assertFalse(is_abundant(70))
    def test_edge_eighty(self):
        self.assertTrue(is_abundant(80))
    def test_edge_ninety(self):
        self.assertFalse(is_abundant(90))
    def test_edge_onehundred(self):
        self.assertTrue(is_abundant(100))
    def test_edge_twohundred(self):
        self.assertFalse(is_abundant(200))
    def test_edge_fivehundred(self):
        self.assertTrue(is_abundant(500))
    def test_edge_one_thousand(self):
        self.assertFalse(is_abundant(1000))
