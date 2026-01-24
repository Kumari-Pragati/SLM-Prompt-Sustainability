import unittest
from mbpp_336_code import check_monthnum

class TestCheckMonthnum(unittest.TestCase):
    def test_february(self):
        self.assertTrue(check_monthnum("February"))

    def test_january(self):
        self.assertFalse(check_monthnum("January"))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_monthnum(123)
