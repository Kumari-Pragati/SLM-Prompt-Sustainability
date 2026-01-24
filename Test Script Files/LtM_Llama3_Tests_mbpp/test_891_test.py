import unittest
from mbpp_891_code import same_Length

class TestSameLength(unittest.TestCase):
    def test_true(self):
        self.assertTrue(same_Length(123, 456))

    def test_false(self):
        self.assertFalse(same_Length(123, 0))

    def test_zero(self):
        self.assertTrue(same_Length(0, 0))

    def test_negative(self):
        self.assertFalse(same_Length(-123, 456))

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            same_Length('123', 456)

    def test_empty(self):
        with self.assertRaises(TypeError):
            same_Length('', 456)
