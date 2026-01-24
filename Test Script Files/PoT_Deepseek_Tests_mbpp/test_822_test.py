import unittest
from mbpp_822_code import pass_validity

class TestPassValidity(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(pass_validity("Abc123$"))
        self.assertTrue(pass_validity("P@ssw0rd"))

    def test_edge_and_boundary_conditions(self):
        self.assertFalse(pass_validity("Abc12"))  # Less than 6 characters
        self.assertFalse(pass_validity("Abc12345678901234567890"))  # More than 12 characters
        self.assertFalse(pass_validity("abc123"))  # No uppercase
        self.assertFalse(pass_validity("ABC123"))  # No lowercase
        self.assertFalse(pass_validity("ABCD123"))  # No special character
        self.assertFalse(pass_validity("Abcdefg"))  # No digit
        self.assertFalse(pass_validity("Abc def"))  # Contains space

    def test_corner_cases(self):
        self.assertFalse(pass_validity(""))  # Empty string
        self.assertFalse(pass_validity("123456"))  # Only digits
        self.assertFalse(pass_validity("ABCDEF"))  # Only uppercase
        self.assertFalse(pass_validity("abcdef"))  # Only lowercase
        self.assertFalse(pass_validity("ABC$"))  # No digit and no space
