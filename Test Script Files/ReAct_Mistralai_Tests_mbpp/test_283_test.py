import unittest
from mbpp_283_code import validate

class TestValidate(unittest.TestCase):

    def test_valid_numbers(self):
        """Test valid numbers with different digits counts"""
        self.assertTrue(validate(123))
        self.assertTrue(validate(12345))
        self.assertTrue(validate(123456789))

    def test_edge_cases(self):
        """Test edge cases with single digits and zero"""
        self.assertTrue(validate(0))
        self.assertTrue(validate(1))
        self.assertTrue(validate(9))

    def test_invalid_numbers(self):
        """Test invalid numbers with repeated digits"""
        self.assertFalse(validate(11))
        self.assertFalse(validate(22))
        self.assertFalse(validate(33))
        self.assertFalse(validate(44))
        self.assertFalse(validate(55))
        self.assertFalse(validate(66))
        self.assertFalse(validate(77))
        self.assertFalse(validate(88))
        self.assertFalse(validate(99))
