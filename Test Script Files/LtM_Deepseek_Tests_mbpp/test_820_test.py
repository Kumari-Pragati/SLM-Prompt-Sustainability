import unittest
from mbpp_820_code import check_monthnum_number

class TestCheckMonthnumNumber(unittest.TestCase):

    def test_simple_valid_input(self):
        self.assertTrue(check_monthnum_number(2))

    def test_edge_case_minimum_value(self):
        self.assertFalse(check_monthnum_number(1))

    def test_edge_case_maximum_value(self):
        self.assertFalse(check_monthnum_number(13))

    def test_typical_invalid_input(self):
        self.assertFalse(check_monthnum_number(0))
        self.assertFalse(check_monthnum_number(15))
