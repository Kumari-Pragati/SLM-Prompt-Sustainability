import unittest
from mbpp_77_code import is_Diff

class TestIsDiff(unittest.TestCase):
    def test_divisible_by_11(self):
        self.assertTrue(is_Diff(22))

    def test_not_divisible_by_11(self):
        self.assertFalse(is_Diff(23))

    def test_zero(self):
        self.assertFalse(is_Diff(0))

    def test_negative_number(self):
        self.assertFalse(is_Diff(-11))

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            is_Diff(22.5)
