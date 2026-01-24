import unittest
from mbpp_283_code import validate

class TestValidateFunction(unittest.TestCase):

    def test_valid_numbers(self):
        self.assertTrue(validate(123))
        self.assertTrue(validate(456))
        self.assertTrue(validate(789))

    def test_invalid_numbers(self):
        self.assertFalse(validate(1111))
        self.assertFalse(validate(2222))
        self.assertFalse(validate(3333))

    def test_edge_cases(self):
        self.assertTrue(validate(0))
        self.assertTrue(validate(1))
        self.assertTrue(validate(9))
        self.assertTrue(validate(10))
        self.assertTrue(validate(99))
        self.assertTrue(validate(100))

    def test_zero(self):
        self.assertTrue(validate(0))

    def test_single_digit(self):
        self.assertTrue(validate(1))
        self.assertTrue(validate(9))

    def test_multiple_digits(self):
        self.assertTrue(validate(12))
        self.assertTrue(validate(34))
        self.assertTrue(validate(56))
        self.assertTrue(validate(78))
        self.assertTrue(validate(90))

    def test_large_numbers(self):
        self.assertTrue(validate(123456))
        self.assertTrue(validate(789012))
        self.assertTrue(validate(3456789))
