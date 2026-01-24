import unittest
from mbpp_598_code import armstrong_number

class TestArmstrongNumber(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertTrue(armstrong_number(153))
        self.assertTrue(armstrong_number(370))

    def test_edge_conditions(self):
        self.assertTrue(armstrong_number(0))
        self.assertFalse(armstrong_number(10))
        self.assertFalse(armstrong_number(100))

    def test_boundary_conditions(self):
        self.assertTrue(armstrong_number(9))
        self.assertFalse(armstrong_number(10))
        self.assertFalse(armstrong_number(100))

    def test_complex_cases(self):
        self.assertFalse(armstrong_number(120))
        self.assertFalse(armstrong_number(351))
        self.assertTrue(armstrong_number(1634))
