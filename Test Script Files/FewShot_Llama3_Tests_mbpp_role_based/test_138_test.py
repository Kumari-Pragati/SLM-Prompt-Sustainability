import unittest
from mbpp_138_code import is_Sum_Of_Powers_Of_Two

class TestIsSumOfPowersOfTwo(unittest.TestCase):
    def test_even_number(self):
        self.assertTrue(is_Sum_Of_Powers_Of_Two(4))

    def test_odd_number(self):
        self.assertFalse(is_Sum_Of_Powers_Of_Two(5))

    def test_zero(self):
        self.assertTrue(is_Sum_Of_Powers_Of_Two(0))

    def test_negative_number(self):
        self.assertFalse(is_Sum_Of_Powers_Of_Two(-4))

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            is_Sum_Of_Powers_Of_Two(4.5)
