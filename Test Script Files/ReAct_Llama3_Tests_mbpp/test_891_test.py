import unittest
from mbpp_891_code import same_Length

class TestSameLength(unittest.TestCase):
    def test_same_length(self):
        self.assertTrue(same_Length(123, 456))

    def test_zero_length(self):
        self.assertTrue(same_Length(0, 0))

    def test_non_zero_length(self):
        self.assertFalse(same_Length(123, 0))

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            same_Length('123', 456)

    def test_negative_input(self):
        self.assertFalse(same_Length(-123, 456))

    def test_long_input(self):
        self.assertTrue(same_Length(123456, 123456))

    def test_edge_case(self):
        self.assertTrue(same_Length(1, 1))
