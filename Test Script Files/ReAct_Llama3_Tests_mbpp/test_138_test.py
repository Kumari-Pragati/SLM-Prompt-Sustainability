import unittest
from mbpp_138_code import is_Sum_Of_Powers_Of_Two

class TestIsSumOfPowersOfTwo(unittest.TestCase):

    def test_even_numbers(self):
        self.assertTrue(is_Sum_Of_Powers_Of_Two(4))
        self.assertTrue(is_Sum_Of_Powers_Of_Two(8))
        self.assertTrue(is_Sum_Of_Powers_Of_Two(16))

    def test_odd_numbers(self):
        self.assertFalse(is_Sum_Of_Powers_Of_Two(1))
        self.assertFalse(is_Sum_Of_Powers_Of_Two(3))
        self.assertFalse(is_Sum_Of_Powers_Of_Two(5))

    def test_zero(self):
        self.assertTrue(is_Sum_Of_Powers_Of_Two(0))

    def test_negative_numbers(self):
        self.assertFalse(is_Sum_Of_Powers_Of_Two(-1))
        self.assertFalse(is_Sum_Of_Powers_Of_Two(-3))
        self.assertFalse(is_Sum_Of_Powers_Of_Two(-5))
