import unittest
from mbpp_283_code import validate

class TestValidate(unittest.TestCase):
    def test_simple_valid(self):
        self.assertTrue(validate(12345))
        self.assertTrue(validate(98765))
        self.assertTrue(validate(11111))

    def test_edge_cases(self):
        self.assertFalse(validate(0))
        self.assertFalse(validate(1111111111))
        self.assertFalse(validate(1234567890))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            validate("12345")
        with self.assertRaises(TypeError):
            validate(None)

    def test_edge_case_invalid(self):
        self.assertFalse(validate(12345678901))
