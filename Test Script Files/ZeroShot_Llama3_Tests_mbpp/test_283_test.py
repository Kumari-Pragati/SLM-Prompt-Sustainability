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
        self.assertFalse(validate(10))

    def test_invalid_input_types(self):
        with self.assertRaises(TypeError):
            validate('abc')
        with self.assertRaises(TypeError):
            validate(None)
