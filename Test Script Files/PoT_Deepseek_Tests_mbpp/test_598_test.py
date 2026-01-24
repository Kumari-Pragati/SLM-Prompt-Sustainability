import unittest
from mbpp_598_code import armstrong_number

class TestArmstrongNumber(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(armstrong_number(153))
        self.assertTrue(armstrong_number(370))

    def test_edge_and_boundary_conditions(self):
        self.assertTrue(armstrong_number(0))
        self.assertFalse(armstrong_number(10))
        self.assertFalse(armstrong_number(100))

    def test_corner_cases(self):
        self.assertFalse(armstrong_number(1234))
        self.assertFalse(armstrong_number(9474))
        self.assertTrue(armstrong_number(9474))  # This is a tricky case where the number is not an Armstrong number but the function should return True
