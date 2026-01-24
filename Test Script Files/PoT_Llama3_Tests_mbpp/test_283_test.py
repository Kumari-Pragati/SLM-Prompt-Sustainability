import unittest
from mbpp_283_code import validate

class TestValidate(unittest.TestCase):

    def test_typical(self):
        self.assertTrue(validate(1234567890))
        self.assertTrue(validate(9876543210))
        self.assertTrue(validate(1111111111))

    def test_edge(self):
        self.assertTrue(validate(123456789))
        self.assertTrue(validate(987654321))
        self.assertTrue(validate(111111111))

    def test_boundary(self):
        self.assertTrue(validate(1234567899))
        self.assertTrue(validate(9876543220))
        self.assertTrue(validate(1111111119))

    def test_invalid(self):
        self.assertFalse(validate(-1234567890))
        self.assertFalse(validate(12345678901))
        self.assertFalse(validate('1234567890'))
