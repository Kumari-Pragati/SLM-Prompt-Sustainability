import unittest
from mbpp_138_code import is_Sum_Of_Powers_Of_Two

class TestIsSumOfPowersOfTwo(unittest.TestCase):
    def test_positive_number(self):
        self.assertTrue(is_Sum_Of_Powers_Of_Two(4))
        self.assertTrue(is_Sum_Of_Powers_Of_Two(6))
        self.assertTrue(is_Sum_Of_Powers_Of_Two(10))
        self.assertTrue(is_Sum_Of_Powers_Of_Two(14))

    def test_zero(self):
        self.assertTrue(is_Sum_Of_Powers_Of_Two(0))

    def test_negative_number(self):
        self.assertFalse(is_Sum_Of_Powers_Of_Two(-1))
        self.assertFalse(is_Sum_Of_Powers_Of_Two(-2))
        self.assertFalse(is_Sum_Of_Powers_Of_Two(-3))
        self.assertFalse(is_Sum_Of_Powers_Of_Two(-4))

    def test_one(self):
        self.assertFalse(is_Sum_Of_Powers_Of_Two(1))
