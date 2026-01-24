import unittest
from mbpp_283_code import validate

class TestValidateFunction(unittest.TestCase):

    def test_normal_input(self):
        self.assertTrue(validate(123456789))
        self.assertTrue(validate(987654321))

    def test_edge_cases(self):
        self.assertTrue(validate(0))
        self.assertTrue(validate(10))
        self.assertTrue(validate(999999999))
        self.assertFalse(validate(1000000000))

    def test_boundary_cases(self):
        self.assertTrue(validate(1))
        self.assertTrue(validate(9))
        self.assertFalse(validate(11))
        self.assertFalse(validate(99))

    def test_invalid_input(self):
        self.assertFalse(validate(-1))
        self.assertFalse(validate(0.5))
        self.assertFalse(validate('str'))
