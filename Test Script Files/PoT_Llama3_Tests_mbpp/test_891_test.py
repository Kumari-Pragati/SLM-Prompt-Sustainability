import unittest
from mbpp_891_code import same_Length

class TestSameLength(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(same_Length(123, 456))

    def test_zero_input(self):
        self.assertTrue(same_Length(0, 0))

    def test_nonzero_input(self):
        self.assertFalse(same_Length(123, 0))

    def test_edge_case(self):
        self.assertTrue(same_Length(12, 12))

    def test_negative_input(self):
        with self.assertRaises(ZeroDivisionError):
            same_Length(-123, -456)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            same_Length('123', 456)
