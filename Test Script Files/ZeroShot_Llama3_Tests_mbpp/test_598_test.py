import unittest
from mbpp_598_code import armstrong_number

class TestArmstrongNumber(unittest.TestCase):

    def test_armstrong_number_true(self):
        self.assertTrue(armstrong_number(153))

    def test_armstrong_number_false(self):
        self.assertFalse(armstrong_number(123))

    def test_armstrong_number_edge_case(self):
        self.assertFalse(armstrong_number(0))

    def test_armstrong_number_negative(self):
        self.assertFalse(armstrong_number(-123))

    def test_armstrong_number_non_integer(self):
        with self.assertRaises(TypeError):
            armstrong_number('123')

    def test_armstrong_number_edge_case_non_integer(self):
        with self.assertRaises(TypeError):
            armstrong_number('0')
