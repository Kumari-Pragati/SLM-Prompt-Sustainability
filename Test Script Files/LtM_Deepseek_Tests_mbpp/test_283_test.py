import unittest
from mbpp_283_code import validate

class TestValidateFunction(unittest.TestCase):

    def test_simple_valid_numbers(self):
        self.assertTrue(validate(12321))
        self.assertTrue(validate(121))
        self.assertTrue(validate(111))

    def test_edge_and_boundary_conditions(self):
        self.assertTrue(validate(0))
        self.assertTrue(validate(9))
        self.assertTrue(validate(10))
        self.assertTrue(validate(99))
        self.assertTrue(validate(100))
        self.assertTrue(validate(999))
        self.assertTrue(validate(1000))
        self.assertTrue(validate(9999))
        self.assertTrue(validate(10000))

    def test_complex_and_corner_cases(self):
        self.assertFalse(validate(112))
        self.assertFalse(validate(1221))
        self.assertFalse(validate(123456))
        self.assertFalse(validate(1234554321))
        self.assertFalse(validate(1234567890))
        self.assertFalse(validate(12345678901))
