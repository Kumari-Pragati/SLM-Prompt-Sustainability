import unittest
from mbpp_283_code import validate

class TestValidate(unittest.TestCase):

    def test_valid_numbers(self):
        self.assertTrue(validate(123))
        self.assertTrue(validate(456))
        self.assertTrue(validate(789))

    def test_invalid_numbers(self):
        self.assertFalse(validate(111))
        self.assertFalse(validate(222))
        self.assertFalse(validate(333))

    def test_edge_cases(self):
        self.assertTrue(validate(0))
        self.assertTrue(validate(1))
        self.assertTrue(validate(9))
        self.assertTrue(validate(99))
        self.assertTrue(validate(999))

    def test_zero(self):
        self.assertTrue(validate(0))

    def test_single_digit(self):
        self.assertTrue(validate(1))
        self.assertTrue(validate(2))
        self.assertTrue(validate(3))
        self.assertTrue(validate(4))
        self.assertTrue(validate(5))
        self.assertTrue(validate(6))
        self.assertTrue(validate(7))
        self.assertTrue(validate(8))
        self.assertTrue(validate(9))

    def test_multiple_digits(self):
        self.assertTrue(validate(12))
        self.assertTrue(validate(23))
        self.assertTrue(validate(34))
        self.assertTrue(validate(45))
        self.assertTrue(validate(56))
        self.assertTrue(validate(67))
        self.assertTrue(validate(78))
        self.assertTrue(validate(89))
        self.assertTrue(validate(90))
