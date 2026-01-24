import unittest
from mbpp_891_code import same_Length

class TestSameLength(unittest.TestCase):

    def test_same_length(self):
        self.assertTrue(same_Length(123, 456))
        self.assertTrue(same_Length(123, 123))
        self.assertFalse(same_Length(123, 12))

    def test_zero_length(self):
        self.assertTrue(same_Length(0, 0))
        self.assertFalse(same_Length(0, 123))

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            same_Length('123', 456)

    def test_non_integer_input2(self):
        with self.assertRaises(TypeError):
            same_Length(123, '456')
