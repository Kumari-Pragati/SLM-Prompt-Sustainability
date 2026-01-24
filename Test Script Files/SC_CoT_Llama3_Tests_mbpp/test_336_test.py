import unittest
from mbpp_336_code import check_monthnum

class TestCheckMonthnum(unittest.TestCase):

    def test_typical_input(self):
        self.assertTrue(check_monthnum("February"))

    def test_edge_case(self):
        self.assertFalse(check_monthnum("January"))

    def test_edge_case2(self):
        self.assertFalse(check_monthnum("March"))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_monthnum(123)

    def test_invalid_input2(self):
        with self.assertRaises(TypeError):
            check_monthnum(None)

    def test_invalid_input3(self):
        with self.assertRaises(TypeError):
            check_monthnum("")

    def test_invalid_input4(self):
        with self.assertRaises(TypeError):
            check_monthnum([1, 2, 3])
