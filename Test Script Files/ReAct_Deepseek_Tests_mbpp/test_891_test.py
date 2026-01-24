import unittest
from mbpp_891_code import same_Length

class TestSameLength(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(same_Length(123, 123))
        self.assertTrue(same_Length(100, 1))
        self.assertFalse(same_Length(123, 456))

    def test_edge_cases(self):
        self.assertTrue(same_Length(0, 0))
        self.assertFalse(same_Length(1, 0))
        self.assertFalse(same_Length(0, 1))

    def test_negative_numbers(self):
        self.assertFalse(same_Length(-123, 123))
        self.assertFalse(same_Length(123, -123))
        self.assertFalse(same_Length(-123, -123))

    def test_non_integer_inputs(self):
        with self.assertRaises(TypeError):
            same_Length(123.5, 123)
        with self.assertRaises(TypeError):
            same_Length(123, 123.5)
        with self.assertRaises(TypeError):
            same_Length(123.5, 123.5)
