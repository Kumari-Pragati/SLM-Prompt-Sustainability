import unittest
from mbpp_283_code import validate

class TestValidateFunction(unittest.TestCase):
    def test_valid_numbers(self):
        self.assertTrue(validate(123456789))
        self.assertTrue(validate(987654321))

    def test_edge_cases(self):
        self.assertTrue(validate(0))
        self.assertTrue(validate(1))
        self.assertTrue(validate(9))
        self.assertTrue(validate(10))

    def test_invalid_inputs(self):
        self.assertFalse(validate(-1))
        self.assertFalse(validate(0.5))
        self.assertFalse(validate('str'))
        self.assertFalse(validate([1, 2, 3]))

    def test_edge_and_boundary_conditions(self):
        self.assertFalse(validate(1111111111))
        self.assertFalse(validate(9999999999))
        self.assertFalse(validate(12345678901))
        self.assertFalse(validate(98765432109))
