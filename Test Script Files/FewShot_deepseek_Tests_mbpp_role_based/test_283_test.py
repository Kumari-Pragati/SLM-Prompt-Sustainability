import unittest
from mbpp_283_code import validate

class TestValidate(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(validate(12321))

    def test_edge_case(self):
        self.assertTrue(validate(0))

    def test_boundary_case(self):
        self.assertTrue(validate(11111))
        self.assertFalse(validate(1234567890))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            validate('123')
